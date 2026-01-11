from sqlalchemy import Column, Integer, String, DateTime
from backend.app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    timezone = Column(String)
    created_at = Column(DateTime)
