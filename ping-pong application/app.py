from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from os import environ

app = FastAPI()

PING_PONG_FILE_PATH = environ.get('PING_PONG_FILE_PATH', './count.txt')

def write_to_disk(string):
    with open(PING_PONG_FILE_PATH, 'w') as file:
        file.write(string)

def read_from_disk():
    with open(PING_PONG_FILE_PATH, 'r') as file:
        return file.read()

write_to_disk('0')


@app.get("/pingpong", response_class=PlainTextResponse)
def respond_pong():
    counter = int(read_from_disk())
    counter += 1
    write_to_disk(str(counter))
    return f"pong {counter}"

@app.get("/pings", response_class=PlainTextResponse)
def get_counter():
    counter = int(read_from_disk())
    return str(counter)