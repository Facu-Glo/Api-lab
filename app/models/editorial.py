from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Editorial(Base):
    __tablename__ = "editorial"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
