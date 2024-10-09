import os
import platform
from rich import print

current_tasks = []
isStart = True


def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r", encoding="utf-8") as file:
            for line in file:
                current_tasks.append(line.strip())


def save_tasks():
    with open("tasks.txt", "w", encoding="utf-8") as file:
        for task in current_tasks:
            file.write(task + "\n")


def add_task():
    print("[bold white]Enter your task: \n")
    new_task = input()
    if new_task == "":
        clear_cmd()
        print("[bold red]Task can't be empty\n")
        add_task()
    else:
        current_tasks.append(new_task)
        save_tasks()
        clear_cmd()
        main()


def remove_task():
    if not current_tasks:
        clear_cmd()
        print("[bold red]You have no tasks to delete\n")
        main()

    print("[bold white]Your tasks: \n")
    for i in range(len(current_tasks)):
        print(str(i + 1) + ".", current_tasks[i])

    try:
        print()
        print("[bold white]Enter number of task to remove: ")
        removed_task = int(input())

        if removed_task < 1 or removed_task > len(current_tasks):
            clear_cmd()
            print("[bold red]Incorrect number of task.\n")
            remove_task()
        else:
            current_tasks.pop(removed_task - 1)
            save_tasks()
            clear_cmd()
            main()

    except ValueError:
        clear_cmd()
        print("[bold red]Write a correct number of task.\n")
        remove_task()


def clear_cmd():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def main(isWrongCommand=None):
    global isStart

    if isWrongCommand is None:
        clear_cmd()
    else:
        print("[bold red]Wrong command\n")
    print("[bold white]To-Do List 🖐\n")

    print("[bold green]1. Add a new task 🟢")
    print("[bold red]2. Remove an existed task 🔴\n")

    if isStart:
        load_tasks()
        isStart = False

    if len(current_tasks) > 0:
        print("[bold white]Your tasks: \n")
        for i in range(len(current_tasks)):
            print(str(i + 1) + ".", current_tasks[i])

    print()
    print("[bold white]Enter command number: \n")
    command = input()
    if command == "1":
        clear_cmd()
        add_task()
    elif command == "2":
        clear_cmd()
        remove_task()
    else:
        clear_cmd()
        main(True)


main()
