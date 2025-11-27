import uuid
import time
from datetime import datetime


random_uuid = uuid.uuid4()

while True:
    current_time = datetime.now()
    print(f'{current_time}: {random_uuid}')
    time.sleep(5)
    