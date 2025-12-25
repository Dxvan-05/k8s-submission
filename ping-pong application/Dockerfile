FROM python:3.11


WORKDIR /app

COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

ENTRYPOINT [ "fastapi", "run", "app.py", "--port", "9090" ]

EXPOSE 9090
