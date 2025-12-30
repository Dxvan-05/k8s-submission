import uuid
from datetime import datetime
from time import sleep

FILE_PATH = '/usr/src/app/files/uuid.txt'

def write_to_disk(string):
    with open(FILE_PATH, 'w') as file:
        file.write(string)


while True:
    random_uuid = uuid.uuid4()
    current_time = datetime.now()
    write_to_disk(f'{current_time} {random_uuid}')
    sleep(5)
