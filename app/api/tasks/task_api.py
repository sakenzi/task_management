from fastapi import Depends, APIRouter, Request, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.tasks.schemas.response import TaskResponse, TaskListResponse
from app.api.tasks.schemas.create import CreateTask
from app.api.tasks.commands.task_crud import create_tasks, get_user_tasks
from database.db import get_db
from utils.context_utils import validate_access_token, get_access_token
from typing import Optional


router = APIRouter()

@router.post(
    "/add-task",
    summary="Создать задачу",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED
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

@router.get(
    "/tasks",
    summary="Получение списка задач пользователя",
    response_model=TaskListResponse
)
async def get_tasks(
    request: Request,
    status: Optional[str] = Query(None),
    sort: str = Query("asc", regex="^(asc|desc)$"),
    db: AsyncSession = Depends(get_db)
):
    access_token = await get_access_token(request)
    user_id = int(await validate_access_token(access_token))
    tasks = await get_user_tasks(db, user_id, status, sort)
    return {"tasks": tasks}