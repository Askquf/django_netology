import uuid

from django.db import models
from django.db.models import CASCADE

class Sensor(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=False)
    description = models.TextField()

class Measurement(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    sensor_id = models.ForeignKey(to=Sensor, on_delete=CASCADE, related_name='measurements')
    temperature = models.IntegerField(null=False)
    date = models.DateTimeField(null=False, auto_now=True)
    image = models.ImageField(null=True)
