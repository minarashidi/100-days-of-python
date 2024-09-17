import requests

params = {
    "amount": 10,
    "category": 18,
    "difficulty": "medium",
    "type": "boolean"
}
response = requests.request(method="GET",
                            url="https://opentdb.com/api.php",
                            params=params)
response.raise_for_status()
data = response.json()
question_data = data['results']
