from pydantic import BaseModel


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class GenreOut(GenreBase):
    id: int
    pass
