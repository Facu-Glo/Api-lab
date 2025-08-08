from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    name: str
    year: int
    id_editorial: int
    id_genre: int
    id_author: int


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    name: Optional[str] = None
    year: Optional[int] = None
    id_editorial: Optional[int] = None
    id_genre: Optional[int] = None
    id_author: Optional[int] = None


class BookOut(BookBase):
    author_name: str | None
    id: int

    model_config = {"from_attributes": True}


class BookDelete(BaseModel):
    detail: str
    book: BookOut
