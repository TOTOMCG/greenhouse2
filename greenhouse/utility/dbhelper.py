from .models import FctRecord, DimComponentType, MapComponent, AvgRecord, Settings


def get_type_id(type_code):
    return DimComponentType.objects.get_or_create(type_code=type_code)[0]


def get_component_id(type_code, device_id):
    return MapComponent.objects.get_or_create(ext_device_id=device_id, type_id=get_type_id(type_code))[0]


def add(type_code, device_id, datetime, value):
    FctRecord.objects.create(component_id=get_component_id(type_code, device_id), datetime=datetime, value=value)


def add_avg(type_code, datetime, value):
    AvgRecord.objects.create(datetime=datetime, type_id=get_type_id(type_code), value=value)


def get(type_code, device_id=0, get_type=''):
    try:
        if get_type == 'avg':
            return AvgRecord.objects.filter(type_id=get_type_id(type_code))
        else:
            return FctRecord.objects.filter(component_id=get_component_id(type_code, device_id))
    except Exception:
        return None


def get_last(type_code, device_id=0, get_type=''):
    g = get(type_code=type_code, device_id=device_id, get_type=get_type)
    if len(g) != 0:
        return g.last().value
    else:
        return 0


def get_chart(type_code):
    r = {'chart_name': type_code, 'chart_type': 'false', 'datetime': [], 'value': []}
    s = []
    match type_code:
        case 'avg_air_hum':
            s.append(get(type_code='air_hum', get_type='avg'))
        case 'air_hum':
            for i in range(1, 5):
                s.append(get(type_code='air_hum', device_id=i))
        case 'avg_temp':
            s.append(get(type_code='temp', get_type='avg'))
        case 'temp':
            for i in range(1, 5):
                s.append(get(type_code='temp', device_id=i))
        case 'soil_hum':
            for i in range(1, 7):
                s.append(get(type_code='soil_hum', device_id=i))
        case 'watering':
            for i in range(1, 7):
                s.append(get(type_code='watering', device_id=i))
            r['chart_type'] = 'true'
        case 'fork_drive':
            s.append(get(type_code='fork_drive', device_id=1))
            r['chart_type'] = 'true'
        case 'total_hum':
            s.append(get(type_code='total_hum', device_id=1))
            r['chart_type'] = 'true'
    for i in range(len(s)):
        a = []
        for c in s[i]:
            if i == 0:
                r['datetime'].append(c.datetime.strftime("%Y-%m-%d %H:%M:%S"))
            a.append(c.value)
        r['value'].append(a)
    return r


def get_table():
    r = []
    dtms = [get('temp', device_id=1).values_list('datetime')]
    for i in range(4):
        dtms.append(get('temp', device_id=i + 1).values_list('value'))
    for i in range(4):
        dtms.append(get('air_hum', device_id=i + 1).values_list('value'))
    for i in range(6):
        dtms.append(get('soil_hum', device_id=i + 1).values_list('value'))
    print(len(dtms))
    for i in range(len(dtms[0])):
        r.append({
            'Время': dtms[0][i][0].strftime("%Y-%m-%d %H:%M:%S"),
            'Температура 1': dtms[1][i][0],
            'Температура 2': dtms[2][i][0],
            'Температура 3': dtms[3][i][0],
            'Температура 4': dtms[4][i][0],
            'Влажность воздуха 1': dtms[5][i][0],
            'Влажность воздуха 2': dtms[6][i][0],
            'Влажность воздуха 3': dtms[7][i][0],
            'Влажность воздуха 4': dtms[8][i][0],
            'Влажность почвы 1': dtms[9][i][0],
            'Влажность почвы 2': dtms[10][i][0],
            'Влажность почвы 3': dtms[11][i][0],
            'Влажность почвы 4': dtms[12][i][0],
            'Влажность почвы 5': dtms[13][i][0],
            'Влажность почвы 6': dtms[14][i][0]
        })
    print(r)
    return {'data': r}


def get_setting(name):
    return Settings.objects.get_or_create(name=name)[0]


def update_setting(name, value):
    setting = get_setting(name)
    setting.value = value
    setting.save()
