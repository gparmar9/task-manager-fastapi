from datetime import datetime
from fastapi import HTTPException, status
from sqlalchemy import func
from .models import Task
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

        return {
            "id": nueva_tarea.id,
            "titulo": nueva_tarea.titulo,
            "contenido": nueva_tarea.contenido,
            "deadline": nueva_tarea.deadline,
            "completada": nueva_tarea.completada,
            "fecha_creacion": nueva_tarea.fecha_creacion
        }

    def obtener_tarea(self, task_id: int):
        # Buscar tarea por ID
        tarea = self.db.query(Task).filter(Task.id == task_id).first()

        # Si no existe la tarea lanzamos un error 404
        if not tarea:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
        
        # Devolvemos lo que espera el modelo de Pydantic
        return {
            "id": tarea.id,
            "titulo": tarea.titulo,
            "contenido": tarea.contenido,
            "deadline": tarea.deadline,
            "completada": tarea.completada,
            "fecha_creacion": tarea.fecha_creacion
        }
    
    def eliminar_tarea(self, task_id: int):
        # Buscar tarea por ID
        tarea = self.db.query(Task).filter(Task.id == task_id).first()

        # Si no existe la tarea lanzamos un error 404
        if not tarea:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
        
        # Eliminamos la tarea
        self.db.delete(tarea)
        self.db.commit()

    def completar_tarea(self, task_id: int):
        # Buscar tarea por ID
        tarea = self.db.query(Task).filter(Task.id == task_id).first()

        # Si no existe la tarea lanzamos un error 404
        if not tarea:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Tarea no encontrada")
        
        # Marcamos como completada la tarea
        tarea.completada = True
        self.db.commit()
        self.db.refresh(tarea)

        # Devolvemos lo que espera el modelo de Pydantic
        return {
            "id": tarea.id,
            "titulo": tarea.titulo,
            "contenido": tarea.contenido,
            "deadline": tarea.deadline,
            "completada": tarea.completada,
            "fecha_creacion": tarea.fecha_creacion
        }

    def obtener_tareas_caducadas(self):
        # Cogemos la fecha actual de cuando se lanza la consulta
        fecha_actual = func.date(datetime.now())

        # Buscamos la lista de tareas caducadas
        tareas_caducadas = self.db.query(Task).filter(func.date(Task.deadline) < fecha_actual).all()

        # Devolvemos lo que espera el modelo Pydantic
        return tareas_caducadas

    def obtener_todas_las_tareas(self):

        # Buscamos la lista de tareas caducadas
        tareas = self.db.query(Task).all()

        # Devolvemos lo que espera el modelo Pydantic
        return tareas


