from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base

# Clase Task para estructura de la BBDD
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    contenido = Column(String, nullable=True)
    deadline = Column(DateTime, nullable=False)
    completada = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime, nullable=False)