from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os 

app = FastAPI()

static_dir = os.path.join(os.path.dirname(__file__), "static")

app.mount("/static", StaticFiles(directory=static_dir), name="static")

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="0.0.0.0", port=8001)

