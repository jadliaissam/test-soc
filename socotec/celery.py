import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socotec.settings')

app = Celery('celery', broker_connection_retry_on_startup=True)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['cine.tasks'])
