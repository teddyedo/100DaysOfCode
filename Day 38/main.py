import requests

APP_ID = "fb7a8c01"
APP_KEY = "08612e6e1c48cb6b3496f584297c0eaa"

EXCERCISE_INFO_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"


def get_burned_cal():
    activity = input("What you did today? ")

    header = {"x-app-id": APP_ID, "x-app-key": APP_KEY,
              "Content-Type": "application/json"}

    parameters = {"query": activity, "gender": "male",
                  "weight_kg": 75, "height_cm": 178, "age": 21}

    response = requests.post(EXCERCISE_INFO_ENDPOINT,
                             params=parameters, headers=header)
    response.raise_for_status()
    print(response.json())


get_burned_cal()
