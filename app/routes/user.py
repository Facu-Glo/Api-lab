# from typing import List
import math
from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.user import UserCreate, UserOut
from app.models.user import User

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/")
def get_users_paginated(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
):
    total = db.query(User).count()
    total_pages = math.ceil(total / limit)
    skip = (page - 1) * limit
    users = db.query(User).offset(skip).limit(limit).all()

    return {
        "total": total,
        "total_pages": total_pages,
        "page": page,
        "limit": limit,
        "results": users,
    }


@router.get("/{user_id}", response_model=UserOut)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not encontrado")
    return user


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user:
        db.delete(user)
        db.commit()
        return {"detail": "User deleted"}
    return {"detail": "User not found"}
