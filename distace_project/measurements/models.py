from django.db import models

# Create your models here.


class Measurement(models.Model):
    location = models.CharField(max_length=200)
    distance = models.CharField(max_length=40)
    destination = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    operation = models.CharField(max_length=200)
    codeName = models.CharField(max_length=20)
    serviceNumber = models.IntegerField()
    station = models.CharField(max_length=100)
    description = models.CharField(max_length=400)

    def __str__(self):
        return f"Distance from {self.location} to {self.destination} is {self.distance} km"
