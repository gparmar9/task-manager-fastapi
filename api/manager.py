from datetime import datetime
from .models import Task
from .database import engine, Base, SessionLocal
from .schemas import TaskCreate, TaskUpdate, TaskResponse

class TaskManager:

    def __init__(self, db):
        self.db = db

    def crear_tarea(self, task: TaskCreate):

        # Crear nueva tarea
        nueva_tarea = Task(
            titulo = task.titulo,
            contenido = task.contenido,
            deadline = task.deadline,
            completada = False,
            fecha_creacion = datetime.now()
        )

        # Guardar tarea en BBDD
        self.db.add(nueva_tarea)
        self.db.commit()
        self.db.refresh(nueva_tarea)
        self.db.close()

        return {
            "id": nueva_tarea.id,
            "titulo": nueva_tarea.titulo,
            "contenido": nueva_tarea.contenido,
            "deadline": nueva_tarea.deadline,
            "completada": nueva_tarea.completada,
            "fecha_creacion": nueva_tarea.fecha_creacion
        }

    def get_task_by_id(self, task_id):
        pass
    
    def complete_task(self, task_id):
        pass

    def get_expired_tasks(self):
        pass