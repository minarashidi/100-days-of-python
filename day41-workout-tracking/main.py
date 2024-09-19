import requests
from datetime import datetime
import os

EXERCISE_TRACKING_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
APPLICATION_ID = os.environ["APPLICATION_ID"]
APPLICATION_KEY = os.environ["APPLICATION_KEY"]
AUTHORIZATION_TOKEN = os.environ["AUTHORIZATION_TOKEN"]

exercise_request_body = {
    "query": input("Tell me which exercises you did: ")
}
headers = {
    'Content-Type': 'application/json',
    'x-app-id': APPLICATION_ID,
    'x-app-key': APPLICATION_KEY
}
exercise_response = requests.request(method="POST", url=EXERCISE_TRACKING_ENDPOINT, json=exercise_request_body,
                                     headers=headers)
exercise_response.raise_for_status()
result = exercise_response.json()

for exercise in result["exercises"]:
    token = {"Authorization": AUTHORIZATION_TOKEN}
    sheet_request_body = {
        "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.request(method="POST", url=SHEET_ENDPOINT, json=sheet_request_body, headers=token)
    sheet_response.raise_for_status()
    print(sheet_response.text)
