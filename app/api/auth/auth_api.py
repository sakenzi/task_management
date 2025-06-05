from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, APIRouter
from database.db import get_db
from app.api.auth.commands.auth_crud import user_register
from app.api.auth.schemas.response import TokenResponse
from app.api.auth.schemas.create import UserRegisterBase


router = APIRouter()

@router.post(
    "/register",
    summary="Регистрация пользователя",
    response_model=TokenResponse
)
async def register(user: UserRegisterBase, db: AsyncSession = Depends(get_db)):
    return await user_register(user=user, db=db)

