from pydantic import BaseModel


class HistoryBase(BaseModel):
    country: str
    city: str


class HistoryCreate(HistoryBase):
    pass


class History(HistoryBase):
    id: int

    class Config:
        orm_mode = True