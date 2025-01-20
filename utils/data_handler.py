import json
import os

def load_habits():
    try:
        with open("data/habits_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_habits(habits, file_path="data/habits_data.json"):
    with open(file_path, "w") as file:
        json.dump(habits, file)

