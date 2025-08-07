from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.db import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    year = Column(Integer, nullable=False)

    id_author = Column(Integer, ForeignKey("author.id"))
    id_editorial = Column(Integer, ForeignKey("editorial.id"))
    id_genre = Column(Integer, ForeignKey("genre.id"))
