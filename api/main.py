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
    # Abrimos sesión
    db = SessionLocal

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Creamos tarea
    nueva_tarea = manager.crear_tarea(task)

    # Cerramos sesion
    db.close()
    return nueva_tarea

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def obtener_tarea_por_id(task_id: int):
    # Abrimos sesión
    db = SessionLocal

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Obtenemos la tarea tarea
    tarea = manager.obtener_tarea(task_id)

    # Cerramos sesion
    db.close()
    return tarea

# @app.put("/tasks/{task_id}/completar", response_model=TaskResponse)
# def marcar_completada(task_id: int):
#     ...

# @app.get("/tasks/caducadas", response_model=List[TaskResponse])
# def obtener_tareas_caducadas():
#     ...

@app.get("/")
def root():
    return {"message": "Task Management API"}
