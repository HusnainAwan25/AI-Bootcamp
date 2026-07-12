from fastapi import FastAPI, HTTPException
from typing import List
from .schemas import TodoCreate, TodoUpdate, TodoResponse

app = FastAPI(
    title="To-Do List API", 
    description="A simple REST API for managing tasks."
)

# ---------------------------------------------------------
# In-Memory Database (Python List)
# ---------------------------------------------------------
todos_db = []
current_id = 1

# ---------------------------------------------------------
# Endpoints
# ---------------------------------------------------------

# Question 1: Add a new task
@app.post("/todos", response_model=TodoResponse, status_code=201)
def create_task(task: TodoCreate):
    global current_id
    new_task = {
        "id": current_id,
        "title": task.title,
        "completed": False
    }
    todos_db.append(new_task)
    current_id += 1
    return new_task

# Question 2: Retrieve all tasks
@app.get("/todos", response_model=List[TodoResponse])
def get_all_tasks():
    return todos_db

# Question 3: Retrieve a specific task by ID
@app.get("/todos/{id}", response_model=TodoResponse)
def get_task(id: int):
    for task in todos_db:
        if task["id"] == id:
            return task
    # Return error if task does not exist
    raise HTTPException(status_code=404, detail="Task not found")

# Question 4: Update an existing task
@app.put("/todos/{id}", response_model=TodoResponse)
def update_task(id: int, task_update: TodoUpdate):
    for task in todos_db:
        if task["id"] == id:
            # Change title if provided
            if task_update.title is not None:
                task["title"] = task_update.title
            # Mark completed if provided
            if task_update.completed is not None:
                task["completed"] = task_update.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Question 5: Delete a task
@app.delete("/todos/{id}")
def delete_task(id: int):
    for index, task in enumerate(todos_db):
        if task["id"] == id:
            del todos_db[index]
            # Return success message
            return {"message": "Task successfully deleted"}
    raise HTTPException(status_code=404, detail="Task not found")