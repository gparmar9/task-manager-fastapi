from fastapi import FastAPI, HTTPException, status
from typing import List
from datetime import datetime

from .database import engine, Base, SessionLocal
from .models import Task
from .schemas import TaskCreate, TaskUpdate, TaskResponse
from .manager import TaskManager
from .logger_config import setup_logger

# Crear tabla en la BBDD
Base.metadata.create_all(bind=engine)

# Configurar logger
logger = setup_logger()

# Crear APP de Fast API
app = FastAPI(title="Gestión de tareas", version="1.0.0")

@app.on_event("startup")
def startup_event():
    logger.info("Iniciando la API de gestión de tareas")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("Apagando la API de gestión de tareas")

@app.post("/tasks/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def crear_tarea(task: TaskCreate):
    logger.info(f"Creando tarea")

    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Creamos tarea
    nueva_tarea = manager.crear_tarea(task)

    # Cerramos sesion
    db.close()

    logger.info(f"Tarea creada")
    
    return nueva_tarea

@app.get("/alltasks", response_model=List[TaskResponse])
def obtener_todas_las_tareas():
    logger.info("Obteniendo todas las tareas")

    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Obtenemos todas las tareas
    tareas = manager.obtener_todas_las_tareas()

    # Cerramos sesion
    db.close()

    logger.info("Todas las tareas obtenidas")

    return tareas

@app.get("/tasks/caducadas", response_model=List[TaskResponse])
def obtener_tareas_caducadas():

    logger.info("Obteniendo tareas caducadas")

    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Obtenemos las tareas caducadas
    tareas_caducadas = manager.obtener_tareas_caducadas()

    # Cerramos sesion
    db.close()

    logger.info("Tareas caducadas obtenidas")

    return tareas_caducadas

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def obtener_tarea_por_id(task_id: int):
    logger.info(f"Obteniendo tarea por ID={task_id}")

    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Obtenemos la tarea tarea
    tarea = manager.obtener_tarea(task_id)

    # Cerramos sesion
    db.close()

    logger.info("Tarea obtenida")
    return tarea

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_tarea(task_id: int):
    logger.info(f"Eliminando tarea con ID={task_id}")
    
    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Eliminamos la tarea
    manager.eliminar_tarea(task_id)

    # Cerramos sesion
    db.close()

    logger.info("Tarea eliminada")

@app.put("/tasks/{task_id}/completar", response_model=TaskResponse)
def completar_tarea(task_id: int):
    logger.info(f"Completando tarea con ID={task_id}")
    # Abrimos sesión
    db = SessionLocal()

    # Instanciamos la clase TaskManager
    manager = TaskManager(db)

    # Eliminamos la tarea
    tarea_completada = manager.completar_tarea(task_id)

    # Cerramos sesion
    db.close()

    logger.info("Tarea completada")

    return tarea_completada

@app.get("/")
def root():
    logger.info("Accediendo a la raiz de la API")
    return {"message": "Task Management API"}
