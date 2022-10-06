from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_validation import UserValidation

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
user_validation = UserValidation()

sheet_data = data_manager.get_destination_data()

cities_without_iata = [row
                       for row in sheet_data if row["iataCode"] == ""]

if len(cities_without_iata) > 0:
    for row in cities_without_iata:
        row["iataCode"] = flight_search.get_iata_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_iata_codes()


for row in sheet_data:
    flight = flight_search.search_flight(row["iataCode"])
    if row["lowestPrice"] > flight.price:
        notification_manager.send_mail("mail", flight)


# user_validation.create_new_user()
