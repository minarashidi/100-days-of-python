import requests
import datetime

# Track how many steps we've walked.

pixela_endpoint = "https://pixe.la/v1/users"

# STEP 1: Create your user account
USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
create_user_request_body = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.request(method="POST", url=pixela_endpoint, json=create_user_request_body)
print(response.text)

# STEP 2: Create your user account - POST - /v1/users/<username>/graphs
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN
}
GRAPH_ID = "graph1"
create_graph_request_body = {
    "id": GRAPH_ID,
    "name": "Track Steps Graph",
    "unit": "steps",
    "type": "int",
    "color": "sora"
}
graph_response = requests.post(create_graph_endpoint, json=create_graph_request_body, headers=headers)
print(graph_response.text)

# STEP 3: Get the graph - /v1/users/<username>/graphs/<graphID>
response = requests.request(method="GET", url=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}")
response.raise_for_status()

# STEP 4: Post value to the graph - /v1/users/<username>/graphs/<graphID>
create_a_pixel_value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
current_date = datetime.datetime.now().strftime("%Y%m%d")
create_pixel_request_body = {
    "date": current_date,
    "quantity": input("How many steps did you walk today?")
}
create_pixel_response = requests.request(method="POST", url=create_a_pixel_value_endpoint,
                                         json=create_pixel_request_body,
                                         headers=headers)
print(create_pixel_response.text)

# STEP 5: update a pixel
# update_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"
# current_date = datetime.datetime.now().strftime("%Y%m%d")
# update_pixel_request_body = {
#     "date": current_date,
#     "quantity": 9000
# }
# update_a_pixel_endpoint = requests.request(method="PUT", url=update_a_pixel_endpoint, json=update_pixel_request_body,
#                                            headers=headers)
# print(update_a_pixel_endpoint.text)

# STEP 6: Delete a pixel
# update_a_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{current_date}"
#
# requests.request(method="DELETE", url=update_a_pixel_endpoint, headers=headers)
