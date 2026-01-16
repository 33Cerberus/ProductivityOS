from datetime import datetime
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