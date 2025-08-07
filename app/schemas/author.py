from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class AuthorOut(AuthorBase):
    id: int
    pass
