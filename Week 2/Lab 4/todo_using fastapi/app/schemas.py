from pydantic import BaseModel
from typing import Optional

# Schema for creating a task (User only provides the title)
class TodoCreate(BaseModel):
    title: str

# Schema for updating a task (Fields are optional so users can update one or both)
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    completed: Optional[bool] = None

# Schema for returning a task (Includes all fields)
class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool