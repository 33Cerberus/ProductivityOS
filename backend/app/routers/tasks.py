from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from backend.app.schemas import TaskCreate, TaskUpdate, TaskOut
from backend.app.crud import create_task, update_task, get_task,  get_tasks, get_tasks_by_user
from backend.app.database import get_db

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task_endpoint(payload: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, user_id=payload.user_id, date=payload.date, description=payload.description)

@router.get("", response_model=List[TaskOut])
def read_tasks_endpoint(user_id: Optional[int] = None, db: Session = Depends(get_db)):
    if user_id is not None:
        return get_tasks_by_user(db, user_id)
    return get_tasks(db)

@router.get("/{task_id}", response_model=TaskOut)
def read_task_endpoint(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskOut)
def update_user_endpoint(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return update_task(db, task, completed=payload.timezone, date=payload.date, description=payload.description)
