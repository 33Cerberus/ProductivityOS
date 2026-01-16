from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from backend.app.schemas import UserCreate, UserUpdate, UserOut
from backend.app.crud import create_user, get_user, get_users, update_user
from backend.app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.post("", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(payload: UserCreate, db: Session = Depends(get_db)):
    existing = get_user(db, payload.id)
    if existing:
        raise HTTPException(status_code=400, detail="User with this ID already exists")
    return create_user(db, user_id=payload.id, timezone_str=payload.timezone)

@router.get("", response_model=List[UserOut])
def read_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)

@router.get("/{user_id}", response_model=UserOut)
def read_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserOut)
def update_user_endpoint(user_id: int, payload: UserUpdate, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return update_user(db, user, timezone_str=payload.timezone)
