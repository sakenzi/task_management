from pydantic import BaseModel, Field
from datetime import datetime
from enum import Enum



class TaskStatus(str, Enum):
    new = "new"
    in_progress = "in_progress"
    done = "done"


class CreateTask(BaseModel):
    title: str = Field(..., max_length=250)
    description: str
    due_date: datetime
    status: TaskStatus = TaskStatus.new