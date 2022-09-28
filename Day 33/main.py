import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 45.436820  # Your latitude
MY_LONG = 10.992851  # Your longitude
MY_EMAIL = "*************@gmail.com"
PASSWORD = "****************"


def is_above_my_house():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        return True
    return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json",
                            params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if datetime.now().hour < sunrise - 2 or datetime.now().hour > sunset + 2:
        return True
    return False


def is_visible():
    return is_above_my_house() and is_dark()


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(MY_EMAIL, "*******************@yahoo.com",
                            msg="Subject:ISS is close\n\n Go out and look up!")


while True:
    time.sleep(60)
    send_email()
