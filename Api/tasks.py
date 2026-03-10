import time
from celery import shared_task




@shared_task
def cache_clear(id):
    print("Cache cleared! IN 10 seconds")
    return id



@shared_task
def add(x, y):
    time.sleep(5)
    return x + y

@shared_task
def sub(x, y):
    time.sleep(6)
    return x - y

