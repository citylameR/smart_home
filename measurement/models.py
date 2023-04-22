from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300,  blank=True)


class Measurement(models.Model):
    sensor_id = models.IntegerField()
    temperature = models.IntegerField()
    data_time = models.IntegerField()
