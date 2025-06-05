from sqlalchemy.ext.asyncio import AsyncSession
from model.models import Task
from app.api.tasks.schemas.create import CreateTask
from sqlalchemy import select, desc, asc
from typing import Optional
from datetime import datetime, timezone


async def create_tasks(db: AsyncSession, user_id: int, task: CreateTask):
    stmt = await db.execute(select(Task))

    new_task = Task(
        title=task.title,
        description=task.description,
        status=task.status,
        due_date=task.due_date,
        user_id=user_id
    )
    db.add(new_task)
    await db.commit()
    await db.refresh(new_task)
    return new_task

async def get_user_tasks(db: AsyncSession, user_id: int, status: Optional[str], sort: str):
    stmt = select(Task).where(Task.user_id == user_id)
    if status:
        stmt = stmt.where(Task.status == status)
    stmt = stmt.order_by(asc(Task.due_date) if sort == "asc" else desc(Task.due_date))
    result = await db.execute(stmt)
    return result.scalars().all()

async def update_task(db: AsyncSession, user_id: int, task_id: int, task_data: CreateTask):
    result = await db.execute(
        select(Task).where(Task.id == task_id, Task.user_id == user_id)
    )
    task = result.scalar_one_or_none()
    if not task:
        return None  

    task.title = task_data.title
    task.description = task_data.description
    task.status = task_data.status
    task.due_date = task_data.due_date

    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, user_id: int, task_id: int):
    result = await db.execute(
        select(Task).where(Task.id == task_id, Task.user_id == user_id)
    )
    task = result.scalar_one_or_none()
    if not task:
        return False

    await db.delete(task)
    await db.commit()
    return True

async def get_user_search_tasks(db: AsyncSession, status: str = None, title: str = None):
    query = select(Task)

    if status:
        query = query.where(Task.status == status)

    if title:
        query = query.where(Task.title.ilike(f"%{title}%"))  

    result = await db.execute(query)
    tasks = result.scalars().all()

    now = datetime.now(timezone.utc)
    for task in tasks:
        task.is_overdue = (task.due_date < now) and (task.status != "done")

    return tasks