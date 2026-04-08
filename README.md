# Task Manager — FastAPI

Aplicación full-stack para la gestión de tareas. Backend con **FastAPI** y **PostgreSQL**, frontend en HTML/JavaScript puro, todo orquestado con **Docker Compose**.

## Tecnologías

| Capa | Tecnología |
|------|-----------|
| Backend | FastAPI 0.135 + SQLAlchemy 2.0 |
| Base de datos | PostgreSQL 16 |
| Frontend | HTML + CSS + JavaScript vanilla |
| Servidor web | Nginx (reverse proxy) |
| Contenedores | Docker Compose |

---

## Arquitectura

```
Browser
  └── :3000  →  Nginx (frontend)
                  ├── /         → index.html
                  └── /api/     → FastAPI (:8080)
                                    └── PostgreSQL (:5432)
```

Los tres servicios se comunican a través de una red Docker interna. El frontend nunca llama directamente al backend — todas las peticiones pasan por Nginx.

---

## Arrancar con Docker (recomendado)

### Requisitos
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución

### Pasos

```bash
# 1. Clonar el repositorio
git clone <url-del-repo>
cd task-manager-fastapi

# 2. Crear el fichero de entorno a partir de la plantilla
cp .env.example .env
# Edita .env y rellena tus credenciales antes de continuar

# 3. Arrancar todos los servicios
docker compose up --build
```

Una vez levantado:

| Servicio | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| API (Swagger UI) | http://localhost:8080/docs |
| API (ReDoc) | http://localhost:8080/redoc |

Para detener: `docker compose down`
Para detener y eliminar los datos: `docker compose down -v`

---

## Arrancar en local (sin Docker)

### Requisitos
- Python 3.11+
- PostgreSQL en ejecución

```bash
# 1. Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar la base de datos en .env
cp .env.example .env
# Edita .env con tus credenciales de PostgreSQL local

# 4. Arrancar la API
uvicorn api.main:app --reload --port 8000
```

La API estará disponible en `http://localhost:8000`.

---

## Endpoints

### `GET /`
Comprueba que la API está activa.

**Respuesta `200`**
```json
{ "message": "API de gestión de tareas funcionando correctamente" }
```

---

### `POST /tasks/`
Crea una nueva tarea.

**Body**
```json
{
  "titulo": "Estudiar FastAPI",
  "contenido": "Repasar endpoints y schemas",
  "deadline": "2026-05-01"
}
```

**Respuesta `201`**
```json
{
  "id": 1,
  "titulo": "Estudiar FastAPI",
  "contenido": "Repasar endpoints y schemas",
  "deadline": "2026-05-01",
  "completada": false,
  "fecha_creacion": "2026-04-08T10:00:00"
}
```

**Errores:** `422` datos inválidos (título vacío, fecha mal formateada, etc.)

---

### `GET /alltasks`
Devuelve todas las tareas.

**Respuesta `200`** — array de tareas (misma estructura que arriba)

---

### `GET /tasks/{task_id}`
Devuelve una tarea por su ID.

**Respuesta `200`** — objeto tarea

**Errores:** `404` si no existe

---

### `PUT /tasks/{task_id}/completar`
Marca una tarea como completada.

**Respuesta `200`**
```json
{
  "id": 1,
  "titulo": "Estudiar FastAPI",
  "contenido": "Repasar endpoints y schemas",
  "deadline": "2026-05-01",
  "completada": true,
  "fecha_creacion": "2026-04-08T10:00:00"
}
```

**Errores:** `404` si no existe

---

### `DELETE /tasks/{task_id}`
Elimina una tarea.

**Respuesta `204`** — sin cuerpo

**Errores:** `404` si no existe

---

### `GET /tasks/caducadas`
Devuelve las tareas cuyo deadline ya ha pasado y no están completadas.

**Respuesta `200`** — array de tareas caducadas

---

## Tests

Los tests son de integración y necesitan la API en ejecución.

```bash
# Con la app corriendo (Docker o local)
python tests/test_api.py
```

Cubren: crear tarea, obtener por ID, completar, obtener caducadas y validación de datos incorrectos.

---

## Estructura del proyecto

```
task-manager-fastapi/
├── api/
│   ├── main.py          # Rutas y app FastAPI
│   ├── manager.py       # Lógica de negocio
│   ├── models.py        # Modelos SQLAlchemy (ORM)
│   ├── schemas.py       # Schemas Pydantic (validación)
│   ├── database.py      # Conexión y sesión de BD
│   └── logger_config.py # Configuración de logging
├── frontend/
│   ├── index.html       # SPA con HTML/CSS/JS
│   ├── nginx.conf       # Reverse proxy config
│   └── Dockerfile
├── tests/
│   └── test_api.py
├── docker-compose.yml
├── Dockerfile
└── requirements.txt
```
