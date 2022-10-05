import requests

READ_SHEET_ENDPOINT = "https://api.sheety.co/c12dc029be876831bcabb98eb45e6af5/flightDeals/prices"
MODIFY_SHEET_ENDPOINT = "https://api.sheety.co/c12dc029be876831bcabb98eb45e6af5/flightDeals/prices/"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(READ_SHEET_ENDPOINT)
        self.destination_data = response.json()["prices"]
        return self.destination_data

    def update_iata_codes(self):
        for row in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": row["iataCode"]
                }
            }

            response = requests.put(
                f"{MODIFY_SHEET_ENDPOINT}/{row['id']}", json=new_data)
            response.raise_for_status()
