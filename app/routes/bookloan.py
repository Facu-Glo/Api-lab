from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.bookloan import BookloanCreate, BookloanOut
from app.database.db import get_db

router = APIRouter(prefix="/bookloan", tags=["bookloan"])


@router.post("/", response_model=BookloanOut)
def create_bookloan(bookloan: BookloanCreate, db: Session = Depends(get_db)):
    db.add(bookloan)
    db.commit()
    db.refresh(bookloan)
    return bookloan


@router.get("/", response_model=List[BookloanOut])
def get_bookloans(db: Session = Depends(get_db)):
    return db.query(BookloanOut).all()
