from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

counter = 0

@app.get("/", response_class=PlainTextResponse)
def get_counter():
    global counter
    counter += 1
    return f"pong {counter}"