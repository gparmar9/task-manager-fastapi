from fastapi import FastAPI, HTTPException, status
from typing import List
from database import engine, Base
from models import Task
from schemas import TaskCreate, TaskUpdate, TaskResponse
from manager import TaskManager

# Crear tabla en la BBDD
Base.metadata.create_all(bind=engine)

# Crear APP de Fast API
app = FastAPI(title="Gestión de tareas", version="1.0.0")

# TODO: Implementar endpoints
# @app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
# def crear_tarea(task: TaskCreate):
#     ...

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
