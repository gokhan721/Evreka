from django.db import models
from django.utils import timezone
# Create your models here.
class Vehicle(models.Model):
    plate = models.CharField(max_length=20)

    def __str__(self):
        return self.plate

class NavigationRecord(models.Model):
    vehicle = models.ForeignKey(
        "navigation_record.Vehicle",
        related_name="navigation_records",
        on_delete=models.CASCADE
    )
    created_time = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        record_dict = dict()
        record_dict["latitude"] = self.latitude
        record_dict["longitude"] = self.longitude
        record_dict["datetime"] = self.created_time.strftime("%d.%m.%Y %H:%M:%S")
        record_dict["vehicle_plate"] = self.vehicle.plate
        return str(record_dict)
