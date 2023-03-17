import requests
from . import dbhelper
from django.utils import timezone

url = 'https://dt.miet.ru/ppo_it/api/'


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


def patch(type_code, device_id, value):
    response = requests.patch(url + type_code, params={'id': device_id, 'state': value},
                              headers={"X-Auth-Token": dbhelper.get_setting('token').value})
    dbhelper.add(type_code, device_id, timezone.localtime(timezone.now()), value)
