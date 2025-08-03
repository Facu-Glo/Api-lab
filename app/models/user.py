from sqlalchemy import Column, Integer, String, Boolean
from app.database.db import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True)
    status = Column(Boolean, default=True)
