from sqlalchemy.ext.asyncio import AsyncSession
from model.models import Task
from app.api.tasks.schemas.create import CreateTask
from sqlalchemy import select, desc, asc
from typing import Optional


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