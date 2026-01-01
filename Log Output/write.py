import uuid
from datetime import datetime
from time import sleep
from os import environ

LOG_OUT_FILE_PATH = environ.get('LOG_OUT_FILE_PATH', './uuid.txt')

def write_to_disk(string):
    with open(LOG_OUT_FILE_PATH, 'w') as file:
        file.write(string)


while True:
    random_uuid = uuid.uuid4()
    current_time = datetime.now()
    write_to_disk(f'{current_time} {random_uuid}')
    sleep(5)
