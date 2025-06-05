from pydantic import BaseModel, Field
from typing import Optional


class UserRegisterBase(BaseModel):
    username: Optional[str] = Field("", max_length=50)
    email: Optional[str] = Field("", max_length=250)
    password: Optional[str] = Field(..., min_length=6)


class UserLoginBase(BaseModel):
    email: str = Field(..., max_length=250)
    password: str = Field(..., min_length=6)