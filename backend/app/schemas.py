from datetime import datetime, date as date_type
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from pydantic import BaseModel, field_validator

class UserCreate(BaseModel):
    id: int
    timezone: str

    @field_validator("timezone")
    @classmethod
    def validate_timezone(cls, tz: str) -> str:
        try:
            ZoneInfo(tz)
        except ZoneInfoNotFoundError:
            raise ValueError("Invalid timezone")
        return tz

class UserUpdate(BaseModel):
    timezone: str

    @field_validator("timezone")
    @classmethod
    def validate_timezone(cls, tz: str) -> str:
        try:
            ZoneInfo(tz)
        except ZoneInfoNotFoundError:
            raise ValueError("Invalid timezone")
        return tz

class UserOut(BaseModel):
    id: int
    timezone: str
    created_at: datetime

    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    user_id: int
    date: date_type
    description: str

    @field_validator("date")
    @classmethod
    def validate_date(cls, date: date_type) -> date_type:
        if not isinstance(date, date_type):
            raise ValueError("Invalid date")
        return date

class TaskUpdate(BaseModel):
    completed: bool
    date: date_type
    description: str

    @field_validator("date")
    @classmethod
    def validate_date(cls, date: date_type) -> date_type:
        if not isinstance(date, date_type):
            raise ValueError("Invalid date")
        return date

class TaskOut(BaseModel):
    id: int
    user_id: int
    date: date_type
    created_at: datetime
    description: str
    completed: bool

    class Config:
        from_attributes = True