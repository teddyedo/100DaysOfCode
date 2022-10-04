import requests

from flight_data import FlightData


class NotificationManager:

    def send_telegram_message(self, message):
        bot_token = "***************************"
        bot_chat_id = "*************************"
        send_text = "https://api.telegram.org/bot" + bot_token + \
            "/sendMessage?chat_id=" + bot_chat_id + "&parse_mode=Markdown&text=" + message

        response = requests.get(send_text)
        response.raise_for_status()

        return response.json()

    def formatMessage(self, flight: FlightData):
        return f"Hurry up! New offer for you!\nFlight to {flight.destination_city} ({flight.destination_airport}) from {flight.departure_city} ({flight.departure_airport}) from {flight.date_from} to {flight.date_to} for only {flight.price} €"
