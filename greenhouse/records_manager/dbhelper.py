from .models import FctRecord, DimComponentType, MapComponent
from django.db.models import Avg


def add(type_code, device_id, datetime, value):
    type_id, b = DimComponentType.objects.get_or_create(type_code=type_code)
    component_id, b = MapComponent.objects.get_or_create(ext_device_id=device_id, type_id=type_id)
    FctRecord.objects.create(component_id=component_id, datetime=datetime, value=value)


def get(type_code, device_id, value):
    type_id = DimComponentType.objects.get(type_code=type_code)
    component_id = MapComponent.objects.get(ext_device_id=device_id, type_id=type_id)
    return FctRecord.objects.filter(component_id=component_id, value=value)

def get_avg():
    get()