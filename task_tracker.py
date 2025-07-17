from task import Task
import json
import sys

class TaskTracker():
    def __init__(self):
        self.tasks = []
        self.last_id = 0
        self._load_from_file()

    def add_task(self, name):
        """Adds a task to tasks list with the name provided and a unique id."""
        self.tasks.append(Task(name=name, id=self.last_id+1))
        self.last_id += 1
        self._save_to_file()

    def update_task(self, id, name):
        """Updates the name of the task with the given id."""
        self._get_task_by_id(id).update_name(name)
        self._save_to_file()

    def mark_task_in_progess(self, id):
        """Sets the status of the task with the given id to 'in-progress'."""
        self._get_task_by_id(id).set_status("in-progress")
        self._save_to_file()

    def mark_task_done(self, id):
        """Sets the status of the task with the given id to 'done'."""
        self._get_task_by_id(id).set_status("done")
        self._save_to_file()

    def mark_task_todo(self, id):
        """Sets the status of the task with the given id to 'todo'."""
        self._get_task_by_id(id).set_status("todo")
        self._save_to_file()

    def delete_task(self, id):
        """Deletes the task with the given id by removing it from the task list."""
        task = self._get_task_by_id(id)
        self.tasks.remove(task)
        del task
        self._save_to_file()

    def get_all_tasks(self):
        """Returns all the tasks in a list of dicts."""
        task_list = []
        for task in self.tasks:
            task_list.append(task.to_dict())
        return task_list
    
    def get_tasks_by_status(self, status):
        """Returns all the tasks with the given status in a list of dicts."""
        if status in ["todo", "done", "in-progress"]:
            task_list = []
            for task in self.tasks:
                if task.get_status() == status:
                    task_list.append(task.to_dict())
            return task_list

        # if status is invalid exit
        print("Invalid Status provided. Options: 'todo', 'done', 'in-progress'")
        sys.exit()

    def _get_task_by_id(self, id):
        for i in range(len(self.tasks)):
            if self.tasks[i].get_id() == id:
                return self.tasks[i]

        # If id not found exit
        print("Id not found.")
        sys.exit()

    def _save_to_file(self):
        with open("tasks.json", "w") as file:
            json.dump({"last_id": self.last_id, "tasks": [task.to_dict() for task in self.tasks]}, file, indent=2)
            

    def _load_from_file(self):
        try:
            with open("tasks.json", "r") as file:
                data = json.load(file)
                self.last_id = data.get("last_id", 0)
                self.tasks = [Task.from_dict(item) for item in data.get("tasks", [])]
        except FileNotFoundError:
            self.tasks = []