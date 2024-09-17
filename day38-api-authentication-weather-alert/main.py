import os

import requests
from twilio.rest import Client

endpoint = "https://pro.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OPEN_WEATHER_MAP_API_KEY")  # free account; "5796abbde9106b7da4febfae8c44c232"
account_sid = "AC3970b9e61977114ec1d01d43989924bd"
auth_token = os.environ.get("OPEN_WEATHER_MAP_AUTH_TOKEN")  # free account; "7469b7a123ef773e003f559ef0213e39"
current_latitude = "59.329323"  # Here you can find it: https://www.latlong.net/
current_longitude = "-18.068581"
cnt = 4  # the number of timestamps in the api response; as we only interested in the next 12 hours(4*3h)

parameters = {
    "lat": current_latitude,
    "lon": current_longitude,
    "appid": api_key,
    "cnt": cnt
}
# Check the weather forcast for the next 12 hours
response = requests.request(method="GET",
                            url=endpoint,
                            params=parameters)

response.raise_for_status()
weather_forcast_data = response.json().get("list")

# check the weather codes: https://openweathermap.org/weather-conditions; if it is less than 700 means we need to take an umbrella
will_rain = False
for data in weather_forcast_data:
    print(f"{data["dt_txt"], data["weather"][0]["main"], data["weather"][0]["id"]}")
    if data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    sms_body = "Bad weather, take your jacket and umbrella!"
    client = Client(account_sid, auth_token)
    # For sending sms, the twilio free tier account only works for US and Canada numbers
    # message = client.messages.create(
    #     body=sms_body,
    #     from_="+12076561743",
    #     to="+46738538038",
    # )

    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body=sms_body,
        to="whatsapp:+46738538038"
    )
