from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    timezone: str
    created_at: datetime