# Importamos los modulos
from pydantic import BaseModel
from typing import Optional

# Creamos la clase de la tarea
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
