from __future__ import absolute_import, unicode_literals

from celery import Celery
from django.utils import timezone
from . import http_request, dbhelper

app = Celery()


@app.task
def get_all():
    t = timezone.localtime()
    avg_value = [0, 0, 0]
    for i in range(1, 5):
        g = http_request.get('temp_hum', i, t)
        avg_value[0] += g[0]
        avg_value[1] += g[1]
    for i in range(1, 7):
        http_request.get('hum', i, t)
    dbhelper.add_avg('temp', t, round(avg_value[0] / 4, 1))
    dbhelper.add_avg('air_hum', t, round(avg_value[1] / 4, 1))
