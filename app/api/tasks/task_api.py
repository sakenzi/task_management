from fastapi import Depends, APIRouter, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.tasks.schemas.response import TaskResponse
from app.api.tasks.schemas.create import CreateTask
from app.api.tasks.commands.task_crud import create_tasks
from database.db import get_db
from utils.context_utils import validate_access_token, get_access_token


router = APIRouter()

@router.post(
    "/add-task",
    summary="Создать задачу",
    response_model=TaskResponse
)
async def add_tasks(
    request: Request,
    body: CreateTask,
    db: AsyncSession = Depends(get_db)
):
    access_token = await get_access_token(request)
    user_id_str = await validate_access_token(access_token)

    try:
        user_id = int(user_id_str)
    except ValueError:
        raise HTTPException(status_code=400, detail="Недопустимый формат идентификатора пользователя в токене")
    
    await create_tasks(db=db, user_id=user_id, task=body)
    return TaskResponse(message="Задача успешно создана")