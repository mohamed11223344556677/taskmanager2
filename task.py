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
    elif command == "list":
        if len(tasks) == 0:
            print("no tasks")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i]["task"])

    elif command == "remove":
        if len(tasks) == 0:
            print("no tasks")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i]["task"])

            number = int(input("enter task number to remove: "))

            if number >= 1 and number <= len(tasks):
                tasks.pop(number - 1)
                save_tasks(tasks)
                print("task removed")
            else:
                print("invalid task number")

    elif command == "exit":
        print("program ended")
        break

    else:
        print("invalid command")