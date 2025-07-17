# Task Tracker

A simple command-line task manager in Python.
Made for [roadmaps.sh](https://roadmap.sh/projects/task-tracker)

### Features

- Add, update, delete tasks
- Set task status: todo, in-progress, or done
- List all tasks
- List tasks by status
- All tasks are saved to `tasks.json`

### Arguments

- `-a`, `--Add` — Add a new task
  **Usage:** `-a "Task name"`

- `-u`, `--Update` — Update an existing task's name
  **Usage:** `-u <id> "New task name"`

- `-d`, `--Delete` — Delete a task by ID
  **Usage:** `-d <id>`

- `--mark-done` — Mark a task as done
  **Usage:** `--mark-done <id>`

- `--mark-in-progress` — Mark a task as in-progress
  **Usage:** `--mark-in-progress <id>`

- `--mark-todo` — Mark a task as todo
  **Usage:** `--mark-todo <id>`

- `-l`, `--List` — List all tasks or filter by status (`todo`, `done`, or `in-progress`)
  **Usage:** `-l` or `-l "status"`

### Example Usage

```bash
python main.py -a "Buy groceries"
python main.py -a "Clean house"
python main.py -a "Clean room"
python main.py -u 1 "Buy milk"
python main.py -d 2
python main.py -mark-done 1
ptyhon main.py -mark-in-progress 3
python main.py -mark-todo 3
python main.py -l
python main.py -l todo
python main.py -l in-progress
python main.py -l done
```

https://roadmap.sh/projects/task-tracker
