import fastapi

from views import home
from views import weather_api
from views import history

api = fastapi.FastAPI()

api.include_router(home.router)
api.include_router(weather_api.router)
api.include_router(history.router)
