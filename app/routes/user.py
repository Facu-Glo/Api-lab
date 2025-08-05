# from typing import List
import math
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.user import UserCreate, UserOut
from app.models.user import User

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
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
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    return UserOut.model_validate(user)
