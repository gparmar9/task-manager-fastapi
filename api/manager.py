from models import Task
from datetime import datetime

class TaskManager:

    def __init__(self, db):
        self.db = db

    def create_task(self, data):

        # Crear nueva tarea
        nueva_tarea = Task(
            titulo = data.titulo,
            contenido = data.contenido,
            deadline = data.deadline,
            completada = False,
            fecha_creacion = datetime.now()
        )

        # Guardar tarea en BBDD
        self.db.add(nueva_tarea)
        self.db.commit()
        self.db.refresh(nueva_tarea)
        self.db.close()

        return {
            "msg": "¡Tarea creada con éxito!",
            "tarea": {
                "id": nueva_tarea.id,
                "titulo": nueva_tarea.titulo,
                "contenido": nueva_tarea.contenido,
                "deadline": nueva_tarea.deadline,
                "completada": nueva_tarea.completada,
                "fecha_creacion": nueva_tarea.fecha_creacion
            }
        }

    def get_task_by_id(self, task_id):
        pass
    
    def complete_task(self, task_id):
        pass

    def get_expired_tasks(self):
        pass