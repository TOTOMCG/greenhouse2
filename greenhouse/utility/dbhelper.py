from .models import FctRecord, DimComponentType, MapComponent, AvgRecord, Settings


def get_type_id(type_code):
    return DimComponentType.objects.get_or_create(type_code=type_code)[0]


def add(type_code, device_id, datetime, value):
    component_id, b = MapComponent.objects.get_or_create(ext_device_id=device_id, type_id=get_type_id(type_code))
    FctRecord.objects.create(component_id=component_id, datetime=datetime, value=value)


def get(type_code, device_id=0, get_type=''):
    try:
        if get_type == 'avg':
            return AvgRecord.objects.filter(type_id=get_type_id(type_code))
        else:
            component_id = MapComponent.objects.get(ext_device_id=device_id, type_id=get_type_id(type_code))
            return FctRecord.objects.filter(component_id=component_id)
    except Exception:
        return None


def get_last(type_code, device_id=0, get_type=''):
    g = get(type_code=type_code, device_id=device_id, get_type=get_type)
    if g is not None:
        return g.last().value
    else:
        return 0


def get_table(type_code):
    r = {'chart_name': type_code, 'datetime': [], 'value': []}
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
        case 'fork_drive':
            s.append(get(type_code='fork_drive', device_id=1))
        case 'total_hum':
            s.append(get(type_code='total_hum', device_id=1))
    for i in range(len(s)):
        a = []
        for c in s[i]:
            if i == 0:
                r['datetime'].append(c.datetime.strftime("%Y-%m-%d %H:%M:%S"))
            a.append(c.value)
        r['value'].append(a)
    return r


def get_setting(name):
    return Settings.objects.get(name=name)


def update_setting(name, value):
    setting = get_setting(name)
    setting.value = value
    setting.save()
