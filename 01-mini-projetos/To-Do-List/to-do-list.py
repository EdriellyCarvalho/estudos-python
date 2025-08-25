import json
from pathlib import Path

tasks_file = Path("tasks.json")

def load_tasks():
    if tasks_file.exists():
        with open(tasks_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(tasks_file, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task "{task}" added to the list.')

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:    
        print("Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")

def remove_task(tasks):
    if not tasks:
        print("No tasks to remove.")
        return
    list_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    print("Welcome to your To-Do List App!")
    while True:
        print("\nMenu: Please choose an option")
        print("1. Add a new Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task(tasks)

        elif choice == '2':
            list_tasks(tasks)

        elif choice == '3':
            remove_task(tasks)

        elif choice == '4':
            print("Exiting the To-Do List App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 