gunicorn -w 1 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8001 app.main:app
