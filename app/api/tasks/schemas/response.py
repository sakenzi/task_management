from pydantic import BaseModel


class TaskResponse(BaseModel):
    message: str = 'Задача успешно создано'

    class Config:
        from_attributes=True