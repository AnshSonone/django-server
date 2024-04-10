from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Airtport(models.Model):
    code = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"({self.code.upper()}) {self.city.capitalize()}"

class Flight(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    origin = models.ForeignKey(Airtport, on_delete=models.CASCADE,  related_name="departures")
    destination  = models.ForeignKey(Airtport, on_delete=models.CASCADE,  related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"FLIGHT{self.id}: FROM {self.origin} TO {self.destination} Trip Time {self.duration}"
    
class Video(models.Model):
    videoName = models.CharField(max_length=200, blank=True)
    video = models.URLField()

    def __str__(self):
        return f"{self.id} {self.videoName.capitalize()} {self.video}"
