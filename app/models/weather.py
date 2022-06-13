from pydantic import BaseModel


class MyWeather(BaseModel):
    temp: float
    description: str