from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import requests
from os import environ

LOG_OUT_FILE_PATH = environ.get('LOG_OUT_FILE_PATH', './uuid.txt')
PING_PONG_URL= environ.get('PING_PONG_URL')
MESSAGE = environ.get('MESSAGE')
INFORMATION_FILE_PATH = environ.get('INFORMATION_FILE_PATH')

app = FastAPI()

def read_file(PATH):
    with open(PATH, 'r') as file:
        file_content = file.read()
        return file_content

def get_count():
    response = requests.get(f'{PING_PONG_URL}/pings')
    count = response.text
    return count

@app.get("/", response_class=PlainTextResponse)
def read_uuid():
    log_output = read_file(LOG_OUT_FILE_PATH)
    ping_pong_count = get_count()
    information_file_message = read_file(INFORMATION_FILE_PATH)

    response_string = f"""
    {log_output}
    Ping / Pongs: {ping_pong_count}
    env variable: MESSAGE = {MESSAGE}
    file content: {information_file_message}
    """

    return response_string