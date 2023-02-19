from __future__ import absolute_import, unicode_literals

import requests
from celery import Celery
from . import dbhelper
from django.utils import timezone

url = 'https://dt.miet.ru/ppo_it/api/'
app = Celery()


def get(type_code, device_id, datetime):
    values = []
    res = requests.get(url + type_code + '/' + str(device_id))
    json = res.json()

    match type_code:
        case 'temp_hum':
            values.append(json['temperature'])
            values.append(json['humidity'])
            dbhelper.add('temp', device_id, datetime, values[0])
            dbhelper.add('air_hum', device_id, datetime, values[1])
        case 'hum':
            values.append(json['humidity'])
            dbhelper.add('soil_hum', device_id, datetime, values[0])
    return values


def patch(token, type_code, value, device_id=0):
    # if device_id:
    #     response = requests.patch(url + type_code, params={'id': device_id, 'state': value},
    #                               headers={"X-Auth-Token:" + token})
    # else:
    #     response = requests.patch(url + type_code, params={'state': value},
    #                               headers={"X-Auth-Token:" + token})
    dbhelper.add(type_code, device_id, timezone.now(), value)


@app.task
def get_all():
    t = timezone.localtime()
    avg_value = [0, 0, 0]
    for i in range(1, 5):
        g = get('temp_hum', i, t)
        avg_value[0] += g[0]
        avg_value[1] += g[1]
    for i in range(1, 7):
        get('hum', i, t)
    dbhelper.add_avg('temp', t, round(avg_value[0] / 4, 1))
    dbhelper.add_avg('air_hum', t, round(avg_value[1] / 4, 1))
