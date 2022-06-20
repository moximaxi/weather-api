from typing import Union
from pydantic import BaseModel


class Location(BaseModel):
    """Pydantic model for location body"""
    city: Union[str, None] = None
    country: Union[str, None] = None
    lat: Union[float, None] = None
    lon: Union[float, None] = None

