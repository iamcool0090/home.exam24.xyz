from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from cachetools import TTLCache
import os 

from app.models.form import ContactForm


cache = TTLCache(maxsize=100, ttl=5)
app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))
static_dir = os.path.join(os.path.dirname(__file__), "static")

app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")


@app.get('/')
async def index(request: Request):
    cache_key = str(request.url)
    if cache_key in cache:
        return cache[cache_key]
    
    response = templates.TemplateResponse("index.html", {"request": request, "name": "John Doe"})
    cache[cache_key] = response
    return response

@app.get('/about')
async def about(request : Request):
    return templates.TemplateResponse("pages/about.html", {"request": request, "name": "John Doe"})


@app.get('/institutions')
async def institutions(request : Request):
    return templates.TemplateResponse("pages/institutions.html", {"request": request, "name": "John Doe"})

@app.post('/contact')
async def contact(email: str = Form(...)):
    form = ContactForm(email=email)
    print(form.email)
    return 200

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request, "name": "John Doe"}, status_code=404)


