from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.database.db import Base


class Bookloan(Base):
    __tablename__ = "bookloans"

    id = Column(Integer, primary_key=True, index=True)
    date_loan = Column(DateTime, nullable=False)
    date_return_expected = Column(DateTime, nullable=True)
    date_returned = Column(DateTime, nullable=True)
    fine = Column(Integer, nullable=True)

    id_boolk = Column(Integer, ForeignKey("books.id"), nullable=False)
    id_user = Column(Integer, ForeignKey("user.id"), nullable=False)
