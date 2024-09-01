import smtplib
import datetime as dt
import random

now = dt.datetime.now()

my_email = "mina.rashidi.86@gmail.com"
password = "<REPLACE YOUR PASSWORD>"

if now.weekday() < 5:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = random.choice(quotes)

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject: Motivational Quote for Today\n\n{quote}")
