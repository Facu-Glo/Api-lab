from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.database.db import get_db
from app.models.book import Book
from app.schemas.book import BookCreate, BookDelete, BookOut, BookUpdate

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
    books = db.query(Book).options(joinedload(Book.author)).all()
    return books


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


@router.delete("/{book_id}", response_model=BookDelete)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.get(Book, book_id)
    if db_book:
        book_out = BookOut.model_validate(db_book)
        db.delete(db_book)
        db.commit()
        return {"detail": "Book deleted", "book": book_out}
    raise HTTPException(status_code=404, detail="Book not found")
