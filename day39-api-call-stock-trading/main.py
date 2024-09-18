import requests
import os
from twilio.rest import Client

STOCK_NAME = "NWARF"
COMPANY_NAME = "Norwegian Air Shuttle ASA"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# Load sensitive data from environment variables
STOCK_API_KEY = os.getenv("STOCK_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")

# STEP 1: Get the yesterday's closing price and compare it with the previous day: https://www.alphavantage.co/documentation/#daily
stock_endpoint_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
response = requests.request(method="GET", url=STOCK_ENDPOINT, params=stock_endpoint_params)
response.raise_for_status()
data = response.json().get("Time Series (Daily)")
stock_data = [value for (key, value) in data.items()]
yesterday_closing_price = float(stock_data[0]["4. close"])
day_before_yesterday_closing_price = float(stock_data[1]["4. close"])

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
percentage_diff = round((difference / float(yesterday_closing_price)) * 100)
print(percentage_diff)

arrow = None
if difference > 0:
    arrow = "🔺"
else:
    arrow = "🔻"

if abs(percentage_diff) > 1:
    # STEP 2: Get the first 3 news articles for the COMPANY_NAME. https://newsapi.org/
    news_endpoint_params = {
        "q": COMPANY_NAME,
        "sortBy": "publishedAt",
        "apiKey": NEWS_API_KEY
    }
    response = requests.request(method="GET", url=NEWS_ENDPOINT, params=news_endpoint_params)
    response.raise_for_status()

    # using Python slice operator to create a list that contains the first 3 articles: https://stackoverflow.com/questions/509211/how-slicing-in-python-works
    first_three_articles = response.json().get("articles", [])[:3]

    # STEP 3: Send message with each article's title and description to your phone number;  twilio.com/docs/sms/quickstart/python
    # articles = [{"title": article.get("title"), "description": article.get("description")} for article in
    #             first_three_articles]
    messages = [f"{COMPANY_NAME}: {percentage_diff} {arrow}\n"
                f"Headline: {article['title']}\n"
                f"Description: {article['description']}"
                for article in first_three_articles]
    for message in messages:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        client.messages.create(
            from_="whatsapp:+14155238886",
            body=message,
            to="whatsapp:+46738538038")
