# To-Do List App

It is a task storing app and it can be mainly used for remembering tasks for a long time and I use this to remember small tasks which I may forget.

## Features

This To-do is a simple app which has the following features:
- Add a task
- Delete a task
- View tasks
- Done vs pending count
- It saves previous entries (tasks) as a txt file
- It loads if data is already present on startup
- Update a task status

## How to Run

Requires Python 3.10 or newer (uses `match/case` syntax).

```
python <file-name>.py
```

## How It Works

- To store the task details, I have used a list of dictionaries to store multiple tasks, with each task holding its own information (title, text, status, date).
- Between sessions, tasks are stored in a text file on the computer. Each task is saved as one line, like `Shopping||Buy a fish|| Pending||08/07/26`, using `||` instead of a comma so that commas typed inside a task's own text don't break the format.
- When a new session starts, the program checks if the text file exists. If it does, it loads the saved tasks; if not (e.g. first time running the app), it just starts with an empty list.
- Limitations: dates are not checked for being real/valid dates, just accepted as text. Status must be entered as exactly `1` or `0` — anything else will cause an error. Tasks are referred to by their position number in the list, so numbers shift after a deletion.

## Example Usage

```
Welcome to Todo
Total Tasks : 0
Choose a Option:
1.Add a task
2.Delete a task
3.View a task
4.Update status
1
Enter the name of task: Shopping
Enter the task details: Buy a fish
Enter the task status(1/0): 0
Enter the date of the task (dd/mm/yy): 08/07/26
Do you want to continue(y/n): y
Welcome to Todo
Total Tasks : 1
Choose a Option:
1.Add a task
2.Delete a task
3.View a task
4.Update status
3
There are total 2 tasks.
Task - 1:
[] --- Shopping:
Task date: 08/07/26
Task:
Buy a fish
Total Tasks : 2 | Done: 0 | Pending: 2
```

## What I'd Improve Next

- Trying to improve more features
- To reduce limitations and errors during input
- Improving data structure by using hash based indexing