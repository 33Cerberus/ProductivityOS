from datetime import datetime
from pydantic import BaseModel

class UserCreate(BaseModel):
    id: int
    timezone: str

class UserUpdate(BaseModel):
    timezone: str

class UserOut(BaseModel):
    id: int
    timezone: str
    created_at: datetime

    class Config:
        orm_mode = True