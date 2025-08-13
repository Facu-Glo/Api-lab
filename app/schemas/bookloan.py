from pydantic import BaseModel


class BookloanBase(BaseModel):
    date_loan: str
    date_return_expected: str
    date_returned: str | None = None
    fine: int

    id_book: int
    id_user: int


class BookloanOut(BookloanBase):
    id: int
    user_name: str

    model_config = {"from_attributes": True}


class BookloanCreate(BookloanBase):
    pass
