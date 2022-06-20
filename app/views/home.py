import fastapi

from fastapi import Depends
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

templates = Jinja2Templates('templates')

router = fastapi.APIRouter()


@router.get('/', response_class = HTMLResponse)
def index(request: Request):
    """Index page"""
    return templates.TemplateResponse('index.html', {'request': request})


@router.get("/login")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    """HTTP Auth"""
    return {"username": credentials.username, "password": credentials.password}




