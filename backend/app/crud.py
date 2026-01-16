from typing import List, Optional
from sqlalchemy.orm import Session
from datetime import date as date_type
from backend.app.models import User, Task

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

def get_users(db: Session) -> List[User]:
    return db.query(User).order_by(User.id).all()

def update_user(db: Session, user: User, timezone_str: Optional[str] = None) -> User:
    if timezone_str is not None:
        user.timezone = timezone_str
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def create_task(db: Session, user_id: int, date: date_type, description: str) -> Task:
    db_task = Task(
        user_id=user_id,
        date=date,
        description=description,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, task_id: int) -> Optional[Task]:
    return db.query(Task).filter(Task.id == task_id).first()

def get_tasks(db: Session) -> List[Task]:
    return db.query(Task).order_by(Task.id).all()

def get_tasks_by_user(db: Session, user_id: int) -> List[Task]:
    return db.query(Task).filter(Task.user_id == user_id).order_by(Task.date).all()

def update_task(db: Session, task: Task,
                completed: Optional[bool] = None,
                date: Optional[date_type] = None,
                description: Optional[str] = None) -> User:
    if completed is not None:
        task.completed = completed
    if date is not None:
        task.date = date
    if description is not None:
        task.description = description
    db.add(task)
    db.commit()
    db.refresh(task)
    return task