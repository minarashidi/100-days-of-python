from datetime import datetime
import smtplib
import time

import requests

my_latitude = 59.329323
my_longitude = 18.068581


# If my position is close to ISS position (+5 or -5)
def is_iss_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    data = iss_response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    if my_latitude - 5 <= iss_latitude <= my_latitude + 5 and my_longitude - 5 <= iss_longitude <= my_longitude + 5:
        return True


# If it's nighttime to be able to see the ISS
def is_nighttime():
    parameters = {
        "lat": my_latitude,
        "lng": my_longitude,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = datetime.now()
    if sunset <= now.hour <= sunrise:
        return True


# Send an email and tell look up
while True:
    time.sleep(60)
    if is_iss_overhead() and is_nighttime():
        my_email = "mina.rashidi.86@gmail.com"
        my_password = "nsuq xwrw kizf uieb"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # Create a connect to email provider
            connection.starttls()  # To secure your connection
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: Look up the ISS \n\n See the ISS {my_email}")
