import fastapi

from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastapi.responses import HTMLResponse

templates = Jinja2Templates('templates')

router = fastapi.APIRouter()

@router.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})




