FROM python:3.13-alpine

LABEL maintainer="Praful M"

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python3", "app/main.py"]