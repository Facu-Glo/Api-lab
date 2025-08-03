from typing import List
from app.database.db import Base, engine, get_db
from fastapi import FastAPI, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, UserOut
from app.models.user import User

# Creo las tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")


# Crear usuario
@app.post("/users/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(name=user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/users/", response_model=List[UserOut])
def get_user(db: Session = Depends(get_db)):
    return db.query(User).all()
