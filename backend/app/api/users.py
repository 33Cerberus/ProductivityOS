from fastapi import APIRouter
from sqlalchemy.orm import Session
from backend.app.models import User as UserModel
from backend.app.database import SessionLocal
from backend.app.schemas import User

router = APIRouter()

@router.post("/register")
def register_user(user_data: User):
    db: Session = SessionLocal()

    db_user = UserModel(
        id=user_data.id,
        timezone=user_data.timezone,
        created_at=user_data.created_at
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()

    return {
        "status": "ok",
        "user_id": db_user.id,
        "message": "User registered successfully"
    }
