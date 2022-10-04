import requests

READ_SHEET_ENDPOINT = "https://api.sheety.co/c12dc029be876831bcabb98eb45e6af5/flightDeals/prices"
MODIFY_SHEET_ENDPOINT = "https://api.sheety.co/c12dc029be876831bcabb98eb45e6af5/flightDeals/prices/"
IATA_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"

FLIGHT_API_KEY = "Dpgz6ODoqCJJO6g_egQmYx-6FLy_Wjiv"


def get_cities_name():
    response = requests.get(READ_SHEET_ENDPOINT)
    return response.json()


def get_IATA_codes(cities):

    for row in cities["prices"]:
        city = row["city"]
        params = {
            "term": city,
            "limit": 10,
            "locale": "en-US",
            "location_types": "airport"
        }
        header = {
            "apikey": FLIGHT_API_KEY
        }

        response = requests.get(IATA_ENDPOINT, params=params, headers=header)
        print(response.json())


get_IATA_codes(get_cities_name())
