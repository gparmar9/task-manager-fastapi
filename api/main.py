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
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Creamos tarea
    nueva_tarea = manager.crear_tarea(task)

    # Cerramos sesion
    db.close()
    return nueva_tarea

@app.get("/tasks/caducadas", response_model=List[TaskResponse])
def obtener_tareas_caducadas():
    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Eliminamos la tarea
    tareas_caducadas = manager.obtener_tareas_caducadas()

    # Cerramos sesion
    db.close()

    return tareas_caducadas

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def obtener_tarea_por_id(task_id: int):
    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Obtenemos la tarea tarea
    tarea = manager.obtener_tarea(task_id)

    # Cerramos sesion
    db.close()
    return tarea

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(task_id: int):
    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Eliminamos la tarea
    manager.eliminar_tarea(task_id)

    # Cerramos sesion
    db.close()

@app.put("/tasks/{task_id}/completar", response_model=TaskResponse)
def completar_tarea(task_id: int):
    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Eliminamos la tarea
    tarea_completada = manager.completar_tarea(task_id)

    # Cerramos sesion
    db.close()

    return tarea_completada

@app.get("/")
def root():
    return {"message": "Task Management API"}
