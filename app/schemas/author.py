from pydantic import BaseModel


class AuthorOut(BaseModel):
    id: int
    name: str
