from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.author import Author
from app.schemas.author import AuthorCreate, AuthorOut

router = APIRouter(prefix="/authors", tags=["Authors"])


@router.post("/", response_model=AuthorOut)
def create_author(author: AuthorCreate, db: Session = Depends(get_db)):
    db_author = Author(**author.model_dump())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


@router.get("/", response_model=list[AuthorOut])
def get_authors(db: Session = Depends(get_db)):
    authors = db.query(Author).all()
    return authors
