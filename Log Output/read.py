from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

FILE_PATH = '/usr/src/app/files/uuid.txt'

app = FastAPI()

def read_file():
    with open(FILE_PATH, 'r') as file:
        file_content = file.read()
        return file_content


@app.get("/", response_class=PlainTextResponse)
def read_uuid():
    file_content = read_file()
    return file_content