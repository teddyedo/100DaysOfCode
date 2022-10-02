import requests
from datetime import datetime, date

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "eorhi4qojhadflgkhj324"
USERNAME = "teddyedo"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# Creating a pixela user

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# requests.post(PIXELA_ENDPOINT, json=user_params)

# Creating a pixel graph

graph_config_params = {
    "id": "graph1",
    "name": "Car distance tracker",
    "unit": "km",
    "type": "float",
    "color": "shibafu"
}

auth_header = {"X-USER-TOKEN": TOKEN}

# requests.post(GRAPH_ENDPOINT, json=graph_config_params, headers=graph_header)

# Populating pixela graph

# requests.post(f"{GRAPH_ENDPOINT}/graph1", json=pixel_params,
# headers=auth_header)

# Modifying an existing pixel

pixel_adjust_params = {
    "quantity": "2"
}

update_endpoint = f"{GRAPH_ENDPOINT}/graph1/{date.today().strftime('%Y%m%d')}"

# requests.put(url=update_endpoint, json=pixel_adjust_params, headers=auth_header)

# Remove a pixel

delete_endpoint = f"{GRAPH_ENDPOINT}/graph1/{date.today().strftime('%Y%m%d')}"

# requests.delete(url=delete_endpoint, headers=auth_header)