from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from os import environ

LOG_OUT_FILE_PATH = environ.get('LOG_OUT_FILE_PATH', './uuid.txt')
PING_PONG_FILE_PATH = environ.get('PING_PONG_FILE_PATH')

app = FastAPI()

def read_file(PATH):
    with open(PATH, 'r') as file:
        file_content = file.read()
        return file_content


@app.get("/", response_class=PlainTextResponse)
def read_uuid():
    log_output = read_file(LOG_OUT_FILE_PATH)
    ping_pong_count = read_file(PING_PONG_FILE_PATH)
    return f'{log_output}\nPing / Pongs: {ping_pong_count}'