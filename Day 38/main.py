import requests
import datetime

APP_ID = "***************"
APP_KEY = "*****************************"

EXERCISE_INFO_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_ENDPOINT = "https://api.sheety.co/****************************/myWorkouts/workouts"


def get_exercise_info():
    activity = input("What you did today? ")

    header = {"x-app-id": APP_ID, "x-app-key": APP_KEY,
              "Content-Type": "application/json"}

    parameters = {"query": activity, "gender": "male",
                  "weight_kg": 75, "height_cm": 178, "age": 21}

    response = requests.post(EXERCISE_INFO_ENDPOINT,
                             json=parameters, headers=header)
    response.raise_for_status()
    return response.json()


def add_a_row(exercise_info):

    header = {
        "Authorization": "Bearer ***************"
    }

    for exercise in exercise_info["exercises"]:
        parameters = {
            "workout": {
                "date": datetime.date.today().strftime("%d-%m-%Y"),
                "time": datetime.datetime.now().strftime("%H:%M:%S"),
                "exercise": exercise["name"].title(),
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }

        response = requests.post(SHEETY_ENDPOINT, json=parameters, headers=header)
        response.raise_for_status()


add_a_row(get_exercise_info())
