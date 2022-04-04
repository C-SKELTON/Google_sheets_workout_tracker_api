import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv("C:/Users/conno/PycharmProjects/.env.txt")

GENDER = "male"
WEIGHT_KG = 90.7185
HEIGHT_CM = 175.26
AGE = 27

APP_ID = os.getenv("Workout_APP_ID")
API_KEY = os.getenv("Workout_API_KEY")

exercise_endpoint = os.getenv("exercise_endpoint")
sheet_endpoint = os.getenv("sheet_endpoint")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
#print(result)

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    workouts = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=workouts, auth=(os.getenv("workout_auth_username"), os.getenv("workout_auth_password")))

    print(sheet_response.text)