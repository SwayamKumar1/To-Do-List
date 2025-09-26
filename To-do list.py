import json
from datetime import datetime


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
    priority = input("Enter task priority (High / Medium / Low): ").strip().lower()
    if priority not in ['high', 'medium', 'low']:
        priority = 'low'
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        due_date = None
    tasks.append({'title': title, 'done': False, 'priority': priority, 'due_date': due_date})

    save_tasks()
    return "Task successfully added."

def show_tasks():
    if not tasks:
        return "No tasks available, add some!"
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. {task['title']} [{status}] Priority: {task.get('priority', 'low').capitalize()} Due: {task.get('due_date') or 'No due date'}")

def search_task(keyword):
    results = [task for task in tasks if keyword.strip().lower() in task['title'].lower()]
    if results:
        for i, task in enumerate(results, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. {task['title']} [{status}] Priority: {task.get('priority', 'low').capitalize()} Due: {task.get('due_date') or 'No due date'}")

    else:
        print("No matching tasks found. ")

def filter_tasks(option):
    if option == "priority":
        chosen = input("Enter priority to filter by (High / Medium / Low):  ").strip().lower()
        results = [task for task in tasks if task.get('priority', 'low') == chosen]
    
    elif option == "status":
        status = input("Enter status to filter by (done / pending): ").strip().lower()
        if status == "done":
            done_value = True
        else:
            done_value = False
        results = [task for task in tasks if task['done'] == done_value]
    elif option == "due_date":
        due_date = input("Enter due date to filter by (YYYY-MM-DD): ").strip()
        results = [task for task in tasks if task.get('due_date') == due_date]
    else:
        print("Invalid filter option.")
        return
    
    if results:
        for i, task in enumerate(results, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. {task['title']} [{status}] Priority: {task.get('priority', 'low').capitalize()} Due: {task.get('due_date') or 'No due date'}")
    else:
        print("No tasks found.")

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
    print("4. Search tasks")
    print("5. Filter tasks")
    print("6. Delete task")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")
    if choice == '1':
        show_tasks()

    elif choice == '2':
        title = input("Enter your task title: ")
        print(add_task(title))

    elif choice == '3':
        title = input("Enter the task title to mark as done:")
        print(mark_done(title))
    
    elif choice == '4':
        keyword = input("Enter keyword to search for: ")
        print(search_task(keyword))
    
    elif choice == '5':
        option = input("Filter by (priority / status / due_date): ").strip().lower()
        filter_tasks(option)

    elif choice == '6':
        title = input("Enter the task title to delete: ")
        print(delete_task(title))

    elif choice == '7':
        print("Exiting the program, Goodbye! ")
        break

    else:
        print("Invalid choice, please try again! ")
