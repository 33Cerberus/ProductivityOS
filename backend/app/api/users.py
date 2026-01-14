from fastapi import APIRouter
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from backend.app.models import User as UserModel
from backend.app.database import SessionLocal
from backend.app.schemas import User

router = APIRouter()

@router.post("/register")
def register_user(user_data: User):
    db: Session = SessionLocal()
    try:
        db_user = db.query(UserModel).filter_by(id=user_data.id).first()

        if db_user:
            db_user.timezone = user_data.timezone
            db_user.created_at = user_data.created_at
            db.commit()
            db.refresh(db_user)
            message = "User updated successfully"
        else:
            db_user = UserModel(
                id=user_data.id,
                timezone=user_data.timezone,
                created_at=user_data.created_at
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            message = "User registered successfully"

        return {
            "status": "ok",
            "user_id": db_user.id,
            "message": message
        }
    except SQLAlchemyError as e:
        db.rollback()
        return {
            "status": "error",
            "message": str(e)
        }
    finally:
        db.close()