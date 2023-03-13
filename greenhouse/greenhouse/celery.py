from __future__ import absolute_import
import os
from datetime import timedelta

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'greenhouse.settings')

app = Celery('greenhouse')

app.config_from_object('django.conf:settings')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'get_all-every-10-seconds': {
        'task': 'utility.tasks.get_all',
        'schedule': timedelta(seconds=10),
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
