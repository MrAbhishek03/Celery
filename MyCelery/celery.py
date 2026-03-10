import os
import time
from celery import Celery
from datetime import timedelta


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyCelery.settings')

app = Celery('MyCelery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule={
    'cache-clear-every-10-seconds': {
        'task': 'Api.tasks.cache_clear',
        # 'schedule': 10,
        'schedule': timedelta(seconds=20),
        'args':('111',)
    },
}