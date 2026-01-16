from typing import List, Optional
from sqlalchemy.orm import Session
from backend.app.models import User

def create_user(db: Session, user_id: int, timezone_str: str) -> User:
    db_user = User(
        id=user_id,
        timezone=timezone_str,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> Optional[User]:
    return db.query(User).filter(User.id == user_id).first()

def list_users(db: Session) -> List[User]:
    return db.query(User).order_by(User.id).all()

def update_user(db: Session, user: User, timezone_str: Optional[str] = None) -> User:
    if timezone_str is not None:
        user.timezone = timezone_str
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
