from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.genre import Genre
from app.schemas.genre import GenreCreate, GenreOut, GenreUpdate

router = APIRouter(prefix="/genres", tags=["Genres"])


@router.post("/", response_model=GenreOut)
def add_genre(genre: GenreCreate, db: Session = Depends(get_db)):
    existing_genre = db.query(Genre).filter(Genre.name == genre.name).first()

    if existing_genre:
        raise HTTPException(status_code=400, detail="Genre already exists")

    genre_data = Genre(**genre.model_dump())
    db.add(genre_data)
    db.commit()
    db.refresh(genre_data)

    return genre_data

@router.get("/", response_model=List[GenreOut])
def get_genres(db: Session = Depends(get_db)):
    return db.query(Genre).all()

@router.put("/{genre_id}", response_model=GenreOut)
def modify_genre(genre_id: int, modify_genre: GenreUpdate, db: Session = Depends(get_db)):
    genre = db.query(Genre).filter(Genre.id == genre_id).first()

    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")

    setattr(genre, "name", modify_genre.name)
    db.commit()
    db.refresh(genre)
    return genre

@router.delete("/genre_id", response_model=GenreOut)
def delete_genre(genre_id: int, db: Session = Depends(get_db)):
    genre = db.get(Genre, genre_id)
    if not genre:
        raise HTTPException(status_code=404, detail="Genre not found")
    db.delete(genre)
    db.commit()
    return genre
