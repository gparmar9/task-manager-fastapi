from fastapi import FastAPI, HTTPException, status
from typing import List
from datetime import datetime

from .database import engine, Base, SessionLocal
from .models import Task
from .schemas import TaskCreate, TaskUpdate, TaskResponse
from .manager import TaskManager

# Crear tabla en la BBDD
Base.metadata.create_all(bind=engine)

# Crear APP de Fast API
app = FastAPI(title="Gestión de tareas", version="1.0.0")

# TODO: Implementar endpoints
@app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(task: TaskCreate):
    
    # Iniciar sesión de BBDD
    db = SessionLocal

    # Crear tarea
    # Crear nueva tarea
    nueva_tarea = Task(
        titulo = task.titulo,
        contenido = task.contenido,
        deadline = task.deadline,
        completada = False,
        fecha_creacion = datetime.now()
    )

    # Guardar tarea en BBDD
    db.add(nueva_tarea)
    db.commit()
    db.refresh(nueva_tarea)
    db.close()

    return {
        "id": nueva_tarea.id,
        "titulo": nueva_tarea.titulo,
        "contenido": nueva_tarea.contenido,
        "deadline": nueva_tarea.deadline,
        "completada": nueva_tarea.completada,
        "fecha_creacion": nueva_tarea.fecha_creacion
    }

# @app.get("/tasks/{task_id}", response_model=TaskResponse)
# def obtener_tarea(task_id: int):
#     ...

# @app.put("/tasks/{task_id}/completar", response_model=TaskResponse)
# def marcar_completada(task_id: int):
#     ...

# @app.get("/tasks/caducadas", response_model=List[TaskResponse])
# def obtener_tareas_caducadas():
#     ...

@app.get("/")
def root():
    return {"message": "Task Management API"}
