import json


try:
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
except FileNotFoundError:
    tasks = []

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    
def mark_done(title):
    title = title.strip().lower()
    for task in tasks:
        if task['title'].strip().lower() == title:
            task['done'] = True
            save_tasks()
            return "Task marked as done."
    return "Task not found."

def add_task(title):
    tasks.append({"title": title, "done": False})
    save_tasks()
    return "Task successfully added."

def show_tasks():
    if not tasks:
        return "No tasks available, add some!"
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. {task['title']} [{status}]")

def delete_task(title):
    global tasks
    before = len(tasks)
    tasks = [task for task in tasks if task['title'].strip().lower() != title.strip().lower()]
    save_tasks()
    return "Task deleted successfully." if len(tasks) < before else "Task not found."

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")
    if choice == '1':
        show_tasks()

    elif choice == '2':
        title = input("Enter your task title: ")
        print(add_task(title))

    elif choice == '3':
        title = input("Enter the task title to mark as done:")
        print(mark_done(title))

    elif choice == '4':
        title = input("Enter the task title to delete: ")
        print(delete_task(title))

    elif choice == '5':
        print("Exiting the program, Goodbye! ")
        break

    else:
        print("Invalid choice, please try again! ")