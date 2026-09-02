import json

filename = "tasks.json"


def load_tasks():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        with open(filename, "w") as file:
            json.dump([], file)
        return []