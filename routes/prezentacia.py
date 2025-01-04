import os
import shutil
from fastapi import APIRouter, File, Form, Request, Depends, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.route import router
# from config.database import client, db, collection_name
from schema.schemas import list_serial, individual_serial_odpoved, individual_serial_portfolio
from datetime import datetime
from utils.functions import get_year, get_image_paths, slugify

router_prezentacia = APIRouter(tags=["prezentacia"])

# Static and template directories
router_prezentacia.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Directory where images are stored
IMAGE_DIR = "static/img"


@router_prezentacia.get("/", response_class=HTMLResponse)
async def home(request: Request, current_year: dict = Depends(get_year)):
    return templates.TemplateResponse("home.html", {"request": request, **current_year})


@router_prezentacia.get("/home-core", response_class=HTMLResponse)
async def home_core(request: Request):
    return templates.TemplateResponse("home_core.html", {"request": request})


@router_prezentacia.get("/honey-extraction", response_class=HTMLResponse)
async def honey_extraction_view(request: Request, current_year: dict = Depends(get_year)):
    """Return the honey extraction page."""
    return templates.TemplateResponse("honey_extraction.html", {"request": request, **current_year})


@router_prezentacia.get("/anatomy", response_class=HTMLResponse)
async def anatomy_view(request: Request, current_year: dict = Depends(get_year)):
    """Return the anatomy page."""
    return templates.TemplateResponse("anatomy.html", {"request": request, **current_year})


@router_prezentacia.get("/anatomy-core", response_class=HTMLResponse)
async def anatomy_core(request: Request):
    return templates.TemplateResponse("anatomy_core.html", {"request": request})

# @router_prezentacia.get("/portfolio_short", response_class=HTMLResponse)
# async def portfolio_view(request: Request, current_year: dict = Depends(get_year)):
#     """Return the portfolio page."""
#     portfolio_data = list_serial(db.portfolio_data.find(), res_func='individual_serial_portfolio')
#     # print(portfolio_data)
#     return templates.TemplateResponse("portfolio_short.html", {"request": request, "portfolio_data": portfolio_data, **current_year})

# @router_prezentacia.get("/portfolio/items", response_class=HTMLResponse)
# async def portfolio_items(request: Request, current_year: dict = Depends(get_year)):
#     """
#     Return the portfolio items page.

#     The page displays a list of portfolio items, including images and descriptions.

#     The data is currently hard-coded for demonstration purposes. In the future, it
#     should be replaced with a database query.
#     """
#     def remove_before_slash(value):
#         if '/' in value:
#             return value.split('/', 1)[1]
#         return value

#     data = list_serial(db.portfolio_data.find(), res_func='individual_serial_portfolio')
#     # PATH = 'templates/projekty'
#     # portfolio_data = [{'title': f, 'path': os.path.join(PATH, f)} for f in os.listdir('templates/projekty')]
#     for projekt in data:
#         projekt['slug'] = os.path.join('projekty', slugify(projekt['title']))
#         projekt['text'] = [p for p in projekt['text'].splitlines() if p != '']
#         # print(projekt)
#         # print(f"updating DB db.hradil.portfolio_data with slug: {projekt['slug']}")   
#         db.portfolio_data.update_one({'title': projekt['title']}, {'$set': {'slug': projekt['slug']}})
#         projekt['slug_id'] = remove_before_slash(projekt['slug'])
#     return templates.TemplateResponse("partials/portfolio_items.html", {"request": request, "portfolio_data": data, **current_year})


# @router_prezentacia.get("/projekty/{slug}", response_class=HTMLResponse)
# async def projekt(request: Request, slug: str, current_year: dict = Depends(get_year)):
#     # print('slug', slug)
#     projekt = individual_serial_portfolio(db.portfolio_data.find_one({'slug': f'projekty/{slug}'}))
#     projekt['text'] = [p for p in projekt['text'].splitlines() if p != '']
#     # print(projekt)
#     return templates.TemplateResponse("projekt.html", {"request": request, "data": projekt, **current_year})

@router_prezentacia.get("/pollinators", response_class=HTMLResponse)
async def pollinators_view(request: Request, current_year: dict = Depends(get_year)):
    """Return the pollinators page."""
    return templates.TemplateResponse("pollinators.html", {"request": request, **current_year})

@router_prezentacia.get("/pollinators-core", response_class=HTMLResponse)
async def pollinators_core(request: Request):
    return templates.TemplateResponse("pollinators_core.html", {"request": request})


@router_prezentacia.get("/science", response_class=HTMLResponse)
async def science_view(request: Request, current_year: dict = Depends(get_year)):
    """Return the science page."""
    return templates.TemplateResponse("science.html", {"request": request, **current_year})

@router_prezentacia.get("/science-core", response_class=HTMLResponse)
async def science_core(request: Request):
    return templates.TemplateResponse("science_core.html", {"request": request})

@router_prezentacia.get("/challenges", response_class=HTMLResponse)
async def challenges_view(request: Request, current_year: dict = Depends(get_year)):
    """Return the challenges page."""
    return templates.TemplateResponse("challenges.html", {"request": request, **current_year})

@router_prezentacia.get("/challenges-core", response_class=HTMLResponse)
async def challenges_core(request: Request):
    return templates.TemplateResponse("challenges_core.html", {"request": request})

@router_prezentacia.get("/lessons", response_class=HTMLResponse)
async def lessons_view(request: Request, current_year: dict = Depends(get_year)):
    """Return the lessons page."""
    return templates.TemplateResponse("lessons.html", {"request": request, **current_year})

@router_prezentacia.get("/lessons-core", response_class=HTMLResponse)
async def lessons_core(request: Request):
    return templates.TemplateResponse("lessons_core.html", {"request": request})
