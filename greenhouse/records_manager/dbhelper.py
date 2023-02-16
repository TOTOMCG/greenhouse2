from .models import FctRecord, DimComponentType, MapComponent, AvgRecord


def add(type_code, device_id, datetime, value):
    type_id, b = DimComponentType.objects.get_or_create(type_code=type_code)
    component_id, b = MapComponent.objects.get_or_create(ext_device_id=device_id, type_id=type_id)
    FctRecord.objects.create(component_id=component_id, datetime=datetime, value=value)


def get(type_code, device_id, value):
    type_id = DimComponentType.objects.get(type_code=type_code)
    component_id = MapComponent.objects.get(ext_device_id=device_id, type_id=type_id)
    return FctRecord.objects.filter(component_id=component_id, value=value)


def add_avg(type_code, datetime, avg_value):
    type_id, b = DimComponentType.objects.get_or_create(type_code=type_code)
    AvgRecord.objects.create(datetime=datetime,type_id=type_id, avg_value=avg_value)