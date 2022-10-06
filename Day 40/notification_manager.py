import requests
import smtplib
from flight_data import FlightData

MY_EMAIL = "***************"
PASSWORD = "*********************"


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

    def send_mail(self, receiver, flight: FlightData):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, PASSWORD)
            connection.sendmail(
                MY_EMAIL, receiver,
                msg=f"Subject:There is an offer for you!\n\n{self.format_email(flight)}".encode("utf-8"))

    def format_email(self, flight: FlightData):
        return f"Hurry up! New offer for you!\nFly to {flight.destination_city} ({flight.destination_airport}) from {flight.departure_city} ({flight.departure_airport}) from {flight.date_from} to {flight.date_to} for only {flight.price} €\n Book here: {flight.book_link}"
