import requests
import json
from datetime import datetime, date, timedelta

BASE_URL = "http://localhost:8000"

# Función para printear info y tener el código más limpio
def print_test_superado(test):
    print(f"Test {test} completado correctamente ✅")

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
    print_test_superado("crear_tarea")


def test_obtener_tarea_por_id(task_id):
    # Consulta al endpoint correspondiente
    response = requests.get(f"{BASE_URL}/tasks/{task_id}")

    # Comprobamos la respuesta de la consulta
    assert response.status_code == 200, f"Esperado 200, obtenido {response.status_code}"
    print_test_superado("obtener_tarea_por_id")

def test_completar_tarea(task_id):
    # Consulta al endpoint correspondiente
    response = requests.put(f"{BASE_URL}/tasks/{task_id}/completar")

    # Comprobamos la respuesta de la consulta
    assert response.status_code == 200, f"Esperado 200, obtenido {response.status_code}"
    print_test_superado("completar_tarea")

def test_obtener_tareas_caducadas():
    # Creamos el payload que manda la consulta como json
    payload = {
        "titulo": "Test tarea caducada",
        "contenido": "Probar el funcionamiento del endpoint de tareas caducadas",
        "deadline": "2026-03-20"
    }

    # Creamos una tarea caducada para asegurarnos que hay una tarea caducada
    tarea_caducada_test = requests.post(f"{BASE_URL}/tasks/", json=payload)

    # Consulta post al endpoint correspondiente para que devuelva las tareas caducadas
    response = requests.get(f"{BASE_URL}/tasks/caducadas")

    # Comprobamos la respuesta de la consulta
    assert response.status_code == 200, f"Esperado 200, obtenido {response.status_code}"
    print_test_superado("obtener_tareas_caducadas")

def test_datos_incorrectos():
    # Payload incorrecto de ejemplo
    payload = {
        "titulo": "",
        "contenido": "Contenido válido"
    }

    # Consulta al endpoint correspondiente
    response = requests.post(f"{BASE_URL}/tasks/", json=payload)

    # Comprobamos la respuesta de la consulta
    assert response.status_code in [400, 422], f"Esperado 400 o 422, obtenido {response.status_code}"
    print_test_superado("test_datos_incorrectos")

if __name__ == "__main__":
    print("Ejecutando tests...")

    test_crear_tarea()
    test_obtener_tarea_por_id(1)
    test_completar_tarea(1)
    test_obtener_tareas_caducadas()
    test_datos_incorrectos()
    
    print("Tests completados")
