import requests
from twilio.rest import Client

API_KEY = "********************************"
SID = "***********************************"
AUTH_TOKEN = "***********************************"

parameters = {"lat": 45.790581, "lon": 20.718349,
              "exclude": "current,daily,minutely",
              "appid": API_KEY}

response = requests.get("https://api.openweathermap.org/data/3.0/onecall",
                        parameters)
response.raise_for_status()
weather_data = response.json()

critics_hours = weather_data["hourly"][:12]

need_an_umbrella = False

for hour in critics_hours:
    for weather_condition in hour["weather"]:
        if weather_condition["id"] < 700:
            need_an_umbrella = True

if need_an_umbrella:
    client = Client(SID, AUTH_TOKEN)
    message = client.messages.create(body="Will rain today", from_="**********",
                                     to="*************")
    print(message.sid)
