import requests

from . import dbhelper
from django.utils import timezone

url = 'https://dt.miet.ru/ppo_it/api/'


def get(type_code, device_id=0):
    if device_id:
        res = requests.get(url + type_code + '/' + str(device_id))
    else:
        res = requests.get(url + type_code)
    json = res.json()
    t = timezone.now()
    if type_code == 'temp_hum':
        dbhelper.add(type_code + '_temp', device_id, t, json['temperature'])
        dbhelper.add(type_code + '_hum', device_id, t, json['humidity'])
    elif type_code == 'hum':
        dbhelper.add(type_code, device_id, t, json['humidity'])

    # return json


def patch(token, type_code, value, device_id=0):
    # if device_id:
    #     response = requests.patch(url + type_code, params={'id': device_id, 'state': value},
    #                               headers={"X-Auth-Token:" + token})
    # else:
    #     response = requests.patch(url + type_code, params={'state': value},
    #                               headers={"X-Auth-Token:" + token})
    dbhelper.add(type_code, device_id, timezone.now(), value)
