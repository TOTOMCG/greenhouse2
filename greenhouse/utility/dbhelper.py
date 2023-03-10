from .models import FctRecord, DimComponentType, MapComponent, AvgRecord, Settings


def get_type_id(type_code):
    return DimComponentType.objects.get_or_create(type_code=type_code)[0]


def add(type_code, device_id, datetime, value):
    component_id, b = MapComponent.objects.get_or_create(ext_device_id=device_id, type_id=get_type_id(type_code))
    FctRecord.objects.create(component_id=component_id, datetime=datetime, value=value)


def get(type_code, device_id):
    component_id = MapComponent.objects.get(ext_device_id=device_id, type_id=get_type_id(type_code))
    return FctRecord.objects.filter(component_id=component_id).last()


def add_avg(type_code, datetime, avg_value):
    AvgRecord.objects.create(datetime=datetime, type_id=get_type_id(type_code), avg_value=avg_value)


def get_avg(type_code):
    return AvgRecord.objects.filter(type_id=get_type_id(type_code)).last()


def get_setting(name):
    return Settings.objects.get(name=name)


def update_setting(name, value):
    get_setting(name).update(value)
