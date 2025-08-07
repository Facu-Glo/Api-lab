from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.book import Book
from app.schemas.book import BookCreate, BookOut, BookUpdate

router = APIRouter(prefix="/books", tags=["Books"])


@router.post("/", response_model=BookOut)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


@router.get("/", response_model=list[BookOut])
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()


@router.get("/{book_id}", response_model=BookOut)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# PUT /books/{id} — Actualizar un libro
@router.put("/{book_id}", response_model=BookOut)
def update_book(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    for key, value in book.model_dump(exclude_unset=True).items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book
