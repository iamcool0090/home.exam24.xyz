from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os 

from app.models.form import ContactForm

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))
static_dir = os.path.join(os.path.dirname(__file__), "static")

app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")


@app.get('/')
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "John Doe"})

@app.get('/about')
async def about(request : Request):
    return templates.TemplateResponse("pages/about.html", {"request": request, "name": "John Doe"})

@app.post('/contact')
async def contact(email: str = Form(...)):
    form = ContactForm(email=email)
    print(form.email)
    return 200



@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request, "name": "John Doe"}, status_code=404)


