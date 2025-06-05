from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import List


class TaskResponse(BaseModel):
    message: str = 'Задача успешно создано'

    class Config:
        from_attributes=True


class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    due_date: datetime
    status: TaskStatus

    class Config:
        from_attributes = True


class TaskListResponse(BaseModel):
    tasks: List[TaskOut]