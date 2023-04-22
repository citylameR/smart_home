from django.contrib import admin

from measurement.models import Sensor, Measurement

@admin.register(Sensor, Measurement)
class SmartHomeAdmin(admin.ModelAdmin):
    pass