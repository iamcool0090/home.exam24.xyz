from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os 

app = FastAPI()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "templates"))
static_dir = os.path.join(os.path.dirname(__file__), "static")

app.mount("/static", StaticFiles(directory=static_dir, html=True), name="static")


@app.get('/')
async def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request, "name": "John Doe"})

@app.get('/about')
async def about(request : Request):
    return templates.TemplateResponse("about.html", {"request": request, "name": "John Doe"})

@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request, "name": "John Doe"}, status_code=404)


if __name__ == "__main__":
    import uvicorn 
    from fastapi.responses import HTMLResponse
    uvicorn.run(app, host="0.0.0.0", port=8001)

