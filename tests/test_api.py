import requests
import json
from datetime import datetime, date, timedelta

BASE_URL = "http://localhost:8000"

def test_crear_tarea():
    # Creamos el payload que manda la consulta como json
    payload = {
        "titulo": "Test crear tarea",
        "contenido": "Probar el endpoint de crear tarea",
        "deadline": "2026-03-26"
    }

    # Consulta post al endpoint correspondiente con el contenido json creado previamente
    response = requests.post(f"{BASE_URL}/tasks/", json=payload)

    # Comprobamos la respuesta de la consulta
    assert response.status_code == 201, f"Esperado 201, obtenido {response.status_code}"
    print("Test crear_tarea completado correctamente ✅")


def test_obtener_tarea():
    """TODO: Implementar test para obtener una tarea por ID"""
    pass

def test_marcar_completada():
    """TODO: Implementar test para marcar una tarea como completada"""
    pass

def test_obtener_tareas_caducadas():
    """TODO: Implementar test para obtener tareas caducadas"""
    pass

def test_datos_incorrectos():
    """TODO: Implementar test con datos incorrectos que debe devolver 400"""
    pass

if __name__ == "__main__":
    print("Ejecutando tests...")
    test_crear_tarea()
    print("Tests completados")
