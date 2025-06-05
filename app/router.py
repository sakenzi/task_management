from fastapi import APIRouter
from app.api.auth.auth_api import router as auth_router
from app.api.tasks.task_api import router as task_router


route = APIRouter()

route.include_router(auth_router, prefix="/auth", tags=["USER_AUTHENTICATION"])
route.include_router(task_router, prefix="/task", tags=["TASKS"])