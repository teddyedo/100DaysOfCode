import requests
import datetime
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "***************************"


class FlightSearch:

    def get_iata_code(self, city_name):

        parameters = {
            "term": city_name,
            "limit": 1,
            "locale": "en-US",
            "location_types": "city"
        }
        header = {
            "apikey": TEQUILA_API_KEY
        }

        response = requests.get(
            TEQUILA_ENDPOINT + "/locations/query", params=parameters, headers=header)
        response.raise_for_status()
        return response.json()["locations"][0]["code"]

    def search_flight(self, destination):

        header = {
            "apikey": TEQUILA_API_KEY
        }

        parameters = {
            "fly_from": "MIL",
            "fly_to": destination,
            "date_from": datetime.date.today().strftime("%d/%m/%Y"),
            "date_to": (datetime.date.today() + datetime.timedelta(days=180)).strftime("%d/%m/%Y"),
            "one_for_city": 1, "flight_type": "round", "nights_in_dst_from": 7,
            "nights_in_dst_to": 28, }

        response = requests.get(
            TEQUILA_ENDPOINT + "/v2/search", params=parameters, headers=header)
        response.raise_for_status()

        data = response.json()["data"][0]

        flight_data = FlightData(
            price=data["price"], departure_city=data["route"][0]["cityFrom"],
            departure_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            date_from=data["route"][0]["local_departure"].split("T")[0],
            date_to=data["route"][1]["local_departure"].split("T")[0])

        return flight_data
