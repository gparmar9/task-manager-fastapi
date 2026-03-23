from models import Task
from datetime import datetime

class TaskManager:

    def __init__(self, db):
        self.db = db

    def create_task(self, data):

        # Crear tarea
        new_task = Task(
            title = data.title,
            content = data.content,
            deadline = data.deadline,
        )

        # Guardar tarea en BBDD
        self.db.add(new_task)
        self.db.commit()
        self.db.refresh(new_task)
        self.db.close()

        return new_task

    def get_task_by_id(self, task_id):
        pass
    
    def complete_task(self, task_id):
        pass

    def get_expired_tasks(self):
        pass