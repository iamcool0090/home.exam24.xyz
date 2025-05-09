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

@app.get('/events')
async def events(request : Request):
    events = [
        {
            "name": "Event 1",
            "date": "2023-10-01",
            "capacity": 100,
            "filled": 50,
            "price": 20.0,
            "local": "Local 1"
        },
        {
            "name": "Event 2",
            "date": "2023-10-02",
            "capacity": 200,
            "filled": 150,
            "price": 30.0,
            "local": "Local 2"
        },
        {
            "name": "Event 3",
            "date": "2023-10-03",
            "capacity": 300,
            "filled": 200,
            "price": 40.0,
            "local": "Local 3"
        },
        {
            "name": "Event 4",
            "date": "2023-10-04",
            "capacity": 400,
            "filled": 350,
            "price": 50.0,
            "local": "Local 4"
        },
        {
            "name": "Event 5",
            "date": "2023-10-05",
            "capacity": 500,
            "filled": 450,
            "price": 60.0,
            "local": "Local 5"
        },
        {
            "name": "Event 6",
            "date": "2023-10-06",
            "capacity": 600,
            "filled": 550,
            "price": 70.0,
            "local": "Local 6"
        },
        {
            "name": "Event 7",
            "date": "2023-10-07",
            "capacity": 700,
            "filled": 650,
            "price": 80.0,
            "local": "Local 7"
        },
        {
            "name": "Event 8",
            "date": "2023-10-08",
            "capacity": 800,
            "filled": 750,
            "price": 90.0,
            "local": "Local 8"
        },
        {
            "name": "Event 9",
            "date": "2023-10-09",
            "capacity": 900,
            "filled": 850,
            "price": 100.0,
            "local": "Local 9"
        },
        {
            "name": "Event 10",
            "date": "2023-10-10",
            "capacity": 1000,
            "filled": 950,
            "price": 110.0,
            "local": "Local 10"
        }
    ]
    return templates.TemplateResponse("events.html", {"request": request, "events": events})


@app.exception_handler(404)
async def not_found(request: Request, exc):
    return templates.TemplateResponse("404.html", {"request": request, "name": "John Doe"}, status_code=404)


if __name__ == "__main__":
    import uvicorn 
    from fastapi.responses import HTMLResponse
    uvicorn.run(app, host="0.0.0.0", port=8001)

