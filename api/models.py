from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base

# Clase Task para estructura de la BBDD
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=True)
    deadline = Column(DateTime, nullable=False)
    completed = Column(Boolean, default=False)