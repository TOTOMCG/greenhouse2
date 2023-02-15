from django.db import models


class DimComponentType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_code = models.CharField(unique=True, max_length=10)


class MapComponent(models.Model):
    component_id = models.AutoField(primary_key=True)
    ext_device_id = models.IntegerField()
    type_id = models.ForeignKey(DimComponentType, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('ext_device_id', 'type_id'),)


class FctRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    component_id = models.ForeignKey(MapComponent, on_delete=models.CASCADE)
    value = models.FloatField()