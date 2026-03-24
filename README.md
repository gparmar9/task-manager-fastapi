# Task Management API

API REST para la gestión de tareas desarrollada con FastAPI.

## Instalación

### 1. Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la aplicación

Puedes usar cualquiera de estos comandos:

```bash
# Opción 1: Comando moderno de FastAPI (recomendado)
fastapi dev main.py

# Opción 2: Uvicorn tradicional
uvicorn main:app --reload
```

La API estará disponible en `http://localhost:8000`

## Endpoints

## 🔹 GET /

### Información de la API

Devuelve un mensaje indicando que la API está activa.

### Respuesta

```json
{
  "message": "API de gestión de tareas funcionando correctamente"
}
```

## 🔹 POST /tasks/

### Crear una nueva tarea

Crea una nueva tarea.

### Body

```json
{
  "titulo": "Estudiar FastAPI",
  "contenido": "Repasar endpoints",
  "deadline": "2026-03-30"
}
```

### Respuesta

```json
{
  "id": 1,
  "titulo": "Estudiar FastAPI",
  "contenido": "Repasar endpoints",
  "deadline": "2026-03-30",
  "completada": false,
  "fecha_creacion": "2026-03-24T10:00:00"
}
```

### Errores

- 422 → Datos inválidos

---

## 🔹 GET /tasks/{task\_id}

### Obtener una tarea por ID

### Respuesta

```json
{
  "id": 1,
  "titulo": "Estudiar FastAPI",
  "contenido": "Repasar endpoints",
  "deadline": "2026-03-30",
  "completada": false,
  "fecha_creacion": "2026-03-24T10:00:00"
}
```

### Errores

- 404 → No encontrada

---

## 🔹 DELETE /tasks/{task\_id}

### Eliminar una tarea

### Respuesta

```json
{
  "message": "Tarea eliminada correctamente"
}
```

### Errores

- 404 → No encontrada

---

## 🔹 PUT /tasks/{task\_id}/completar

### Marcar tarea como completada

### Respuesta

```json
{
  "id": 1,
  "titulo": "Estudiar FastAPI",
  "contenido": "Repasar endpoints",
  "deadline": "2026-03-30",
  "completada": true,
  "fecha_creacion": "2026-03-24T10:00:00"
}
```

### Errores

- 404 → No encontrada

---

## 🔹 GET /tasks/caducadas

### Obtener tareas caducadas

Devuelve tareas cuyo deadline ya ha pasado.

### Respuesta

```json
[
  {
    "id": 2,
    "titulo": "Tarea vencida",
    "contenido": "Esto ya pasó",
    "deadline": "2026-03-20",
    "completada": false,
    "fecha_creacion": "2026-03-18T09:00:00"
  }
]
```

---

## Ejecutar tests

```bash
python test_api.py
```

## Documentación interactiva

Una vez ejecutando la aplicación, puedes acceder a:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
