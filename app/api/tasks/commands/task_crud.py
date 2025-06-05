from sqlalchemy.ext.asyncio import AsyncSession
from model.models import Task
from app.api.tasks.schemas.create import CreateTask
from sqlalchemy import select


async def create_tasks(db: AsyncSession, user_id: int, task: CreateTask):
    stmt = await db.execute(select(Task))
    existing_task = stmt.scalar_one_or_none()

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