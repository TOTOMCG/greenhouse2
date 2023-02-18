from django.db import models

class settings(models.Model):
    setting_name = models.CharField(unique=True, max_length=12)
    setting_value = models.FloatField()

