gunicorn -w 2 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8002 app.main:app
