from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.genre import Genre
from app.schemas.genre import GenreOut

router = APIRouter(prefix="/genres", tags=["Genres"])


@router.post("/", response_model=GenreOut)
def add_genre(name: str, db: Session = Depends(get_db)):
    existing_genre = db.query(Genre).filter(Genre.name == name).first()
    if existing_genre:
        raise HTTPException(status_code=400, detail="Genre already exists")
    new_genre = Genre(name=name)
    db.add(new_genre)
    db.commit()
    db.refresh(new_genre)
    return new_genre


@router.get("/", response_model=List[GenreOut])
def get_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()
