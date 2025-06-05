from pydantic import BaseModel
from datetime import datetime


class TokenResponse(BaseModel):
    access_token: str
    access_token_type: str = 'Bearer'
    access_token_expire_time: datetime