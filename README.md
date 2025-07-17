# Task Tracker

A simple command-line task manager in Python.

### Features

- Add, update, delete tasks
- Set task status: todo, in-progress, or done
- List tasks by status
- All tasks are saved to `tasks.json`

### Usage

```bash
python main.py -a "Buy groceries"
python main.py -u 0 "Buy milk"
python main.py -d 0
python main.py --mark-done 1
python main.py --List
```
