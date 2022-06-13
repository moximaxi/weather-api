import fastapi
import httpx

from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse

templates = Jinja2Templates('templates')

from models.location import Location
from models.weather import MyWeather

router = fastapi.APIRouter()

@router.get('/api/weather', response_class=HTMLResponse)
async def weather(request: Request, location: Location = fastapi.Depends()):
    url = f'https://weather.talkpython.fm/api/weather?city={location.city}&country={location.country}&units=metric'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    weather = data.get('weather', {})
    description = weather.get('description', "sunny")
    forecast = data.get('forecast', {})
    temp = forecast.get('temp', 0.0)

    city = location.city

    myweather = MyWeather(temp=temp, description=description)

    return templates.TemplateResponse('weather.html', {'request': request, 'temp' : temp, 'description' : description, 'city' : city})