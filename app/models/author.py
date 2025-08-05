from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
