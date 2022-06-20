from sqlalchemy import Column, Integer, String

from .database import Base


class History(Base):
    """SQLalchemy DB class for history"""
    __tablename__ = "history"

    id = Column(Integer, primary_key = True, index = True)
    country = Column(String)
    city = Column(String)
