import fastapi
import httpx

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from starlette.requests import Request

from models.location import Location


templates = Jinja2Templates('templates')

router = fastapi.APIRouter()


@router.get('/api/weather', response_class = HTMLResponse)
async def weather(request: Request, location: Location = fastapi.Depends()):
    """Get weather data with city name"""
    url = f'https://weather.talkpython.fm/api/weather?city={location.city}'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    weather = data.get('weather', {})
    description = weather.get('description')
    forecast = data.get('forecast', {})
    temp = forecast.get('temp')

    return templates.TemplateResponse('weather.html', {
            'request': request, 
            'temp': temp, 
            'description': description,
            'city': location.city
        })


@router.get('/api/weather/coords', response_class = HTMLResponse)
async def weather(request: Request, location: Location = fastapi.Depends()):
    """Get weather data with coords"""
    API_KEY = "4bf39665989d4e8da348b4afa1b3218c"

    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={location.lat}&lon={location.lon}&appid={API_KEY}&units=metric'

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    current = data.get('current', {})
    weather = current.get('weather', {})
    description = weather[0].get('description')
    temp = current.get('temp')

    return templates.TemplateResponse('weather_coords.html', {
            'request': request,
            'temp': temp,
            'description': description,
            'lat': location.lat,
            'lon': location.lon,
        })
