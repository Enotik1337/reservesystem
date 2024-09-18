from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hall(models.Model):
    types = [
        ("Common PC", "Common PC"),
        ("PlayStation", "PlayStation"),
        ("VR", "VR")
    ]
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    type = models.CharField(max_length=11, choices=types)

class Place(models.Model):
    number = models.IntegerField()
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name="places")

class Booking(models.Model):
    timestart = models.DateTimeField()
    timeend = models.DateTimeField()
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="booking")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking")