import json
import os

def load_habits():
    try:
        with open("data/habits_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_habits(habits_data):
    os.makedirs("data", exist_ok=True)
    with open("data/habits_data.json", "w") as file:
        json.dump(habits_data, file)
