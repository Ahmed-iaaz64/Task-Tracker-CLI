class Task():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.status = "todo"

    def update_name(self, name):
        self.name = name

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id
    
    def set_status(self, status):
        self.status = status
    
    def get_status(self):
        return self.status
    
    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data):
        task = Task(data["name"], data["id"])
        task.set_status(data["status"])
        return task

    def __str__(self):
        return self.name
    