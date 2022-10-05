class FlightData:

    def __init__(self, departure_city, departure_airport, destination_city, destination_airport, price, date_from, date_to, stop_overs=0, via_city=""):
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.price = price
        self.date_from = date_from
        self.date_to = date_to
        self.stop_overs = stop_overs
        self.via_city = via_city
