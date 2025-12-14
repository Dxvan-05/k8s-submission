import uuid
from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

random_uuid = uuid.uuid4()

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def read_uuid():
    current_time = datetime.now()
    return f'{current_time} {random_uuid}'
