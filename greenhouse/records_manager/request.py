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
            dbhelper.add(type_code + '_temp', device_id, datetime, values[0])
            dbhelper.add(type_code + '_hum', device_id, datetime, values[1])
        case 'hum':
            values.append(json['humidity'])
            dbhelper.add(type_code, device_id, datetime, values[0])
    return values


def patch(token, type_code, value, device_id=0):
    # if device_id:
    #     response = requests.patch(url + type_code, params={'id': device_id, 'state': value},
    #                               headers={"X-Auth-Token:" + token})
    # else:
    #     response = requests.patch(url + type_code, params={'state': value},
    #                               headers={"X-Auth-Token:" + token})
    dbhelper.add(type_code, device_id, timezone.now(), value)


def get_all():
    t = timezone.now()
    avg_value = [0, 0, 0]
    for i in range(1, 5):
        g = get('temp_hum', i, t)
        avg_value[0] += g[0]
        avg_value[1] += g[1]
    for i in range(1, 7):
        avg_value[2] += get('hum', i, t)[0]
    dbhelper.add_avg('temp_hum_temp', t, avg_value[0] / 4)
    dbhelper.add_avg('temp_hum_hum', t, avg_value[1] / 4)
    dbhelper.add_avg('hum', t, avg_value[2] / 4)
    print(getattr(dbhelper.get('hum', 1), 'value'))
