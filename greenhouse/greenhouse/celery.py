from __future__ import absolute_import
import os
from datetime import timedelta

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greenhouse.settings')

app = Celery('greenhouse')
app.config_from_object(settings, namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get_all-every-10-seconds': {
        'task': 'records_manager.tasks.get_all',
        'schedule': timedelta(seconds=3),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
