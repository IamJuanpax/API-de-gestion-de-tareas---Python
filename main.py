# API de gestion de tareas

# Importamos los modulos
from fastapi import FastAPI, HTTPException
from models import Task

# Inicializamos la api
app = FastAPI()

# Base de datos en memoria (lista)
tasks = []

# Agregar una tarea a la lista
@app.post("/tasks/", response_model=Task)
def create_task(task: Task):
    # Agregar la nueva tarea a la lista
    tasks.append(task)
    return task

# Devolver las tareas de la lista
@app.get("/tasks/", response_model=list[Task])
def get_tasks():
    return tasks

# Devolver una tarea especifica
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = next((t for t in tasks if t.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Actualizar una tarea
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# Borrar una tarea
@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            deleted_task = tasks.pop(index)
            return deleted_task
    raise HTTPException(status_code=404, detail="Task not found")
