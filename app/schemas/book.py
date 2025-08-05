from pydantic import BaseModel


class BookBase(BaseModel):
    name: str
    year: int
    id_editorial: int
    id_genre: int
    id_author: int


class BookCreate(BookBase):
    pass


class BookOut(BookBase):
    id: int

    model_config = {"from_attributes": True}
