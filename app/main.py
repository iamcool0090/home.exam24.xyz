from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os 

app = FastAPI()
templates = Jinja2Templates(directory="templates")
static_dir = os.path.join(os.path.dirname(__file__), "static")

app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")


@app.get('/')
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "John Doe"})

@app.get('/about')
async def about(request : Request):
    return templates.TemplateResponse("about.html", {"request": request, "name": "John Doe"})




if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8001)

