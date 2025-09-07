# 📝 To-Do List (Mini-Project)

A simple command-line **To-Do List Manager** built with Python.  
This project demonstrates **JSON file handling**, **data persistence**, and basic CRUD operations (Create, Read, Update, Delete).

---

## 📌 Features
- ✅ Add new tasks  
- 📋 Show all tasks with status (✓ done / ✗ pending)  
- ✏️ Mark tasks as done  
- ❌ Delete tasks  
- 💾 Persistent storage using `tasks.json` (tasks are saved even after the program exits)

---

## ⚙️ How It Works
- All tasks are stored as dictionaries inside a list, like:
  ```json
  [
    {"title": "Buy milk", "done": false},
    {"title": "Finish homework", "done": true}
  ]
The list is written to and read from tasks.json using Python’s built-in json module.

## Tech Stack
Python 3

JSON (for file-based storage)

## How to Run
Clone the repo:

Copy code
git clone https://github.com/yourusername/todo-list.git
cd todo-list

Run the script:

python "To-do list.py
## Learning Outcome
Through this mini-project, I practiced:

-File handling in Python (open, read, write)
-JSON serialization (json.dump, json.load)
-Menu-driven CLI applications
-Implementing basic CRUD logic
