from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from cachetools import TTLCache
import os 

from app.models.form import ContactForm
from app.database.db_sqlite import SQLiteDatabase
from app.models.lead import Lead

from typing import Any

cache = TTLCache(maxsize=100, ttl=5)
app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))
db = SQLiteDatabase('data.sql')

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
    db.execute_query("INSERT INTO leads (email, created_at) VALUES (?, datetime('now'))", (form.email,))
    db.connection.commit()
    return 200

@app.get('/leads')
async def leads(request: Request):
    leads = db.execute_query("SELECT * FROM leads")
    return templates.TemplateResponse("pages/leads.html", {"request": request, "leads": leads, "name": "John Doe"})

@app.post('/leads')
async def create_lead(email: str = Form(...)):
    try:
        cursor = db.get_cursor()
        cursor.execute("INSERT INTO leads (email, created_at) VALUES (?, datetime('now'))", (email,))
        cursor.connection.commit()
        cursor.close()

        leads = db.execute_query("SELECT * FROM leads")
        leads_list = [Lead.factory(row) for row in leads]
        
        return templates.TemplateResponse("pages/leads.html", {"request": {}, "leads": leads_list}, status_code=200)
    


    except Exception as e:
        return {"error": str(e)}

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request, "name": "John Doe"}, status_code=404)


