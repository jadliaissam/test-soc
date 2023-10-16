import time

from celery import shared_task


@shared_task
def send_review():
    print('Sending review in progress .....')
    for i in range(10):
        print(f'Task will end in {10 - i} seconds')
        time.sleep(1)
    print('Review sent')
