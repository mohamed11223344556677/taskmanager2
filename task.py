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


tasks = load_tasks()
def save_tasks(tasks):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)


while True:
    command = input("enter command: ")

    if command == "add":
        task = input("enter task: ")
        tasks.append({"task": task})
        save_tasks(tasks)
        print("task added")