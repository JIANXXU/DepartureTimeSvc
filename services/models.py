from django.db import models

# Create your models here.

class DepartureTime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    agencyName = models.CharField(max_length=100, blank=True, default='')
    routeName = models.CharField(max_length=100, blank=True, default='')
    stopName = models.CharField(max_length=100, blank=True, default='')
    stopCode = models.IntegerField(default=0)
    nextDepartureTime = models.IntegerField(default=-1)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        ordering = ('created',)


class Location(models.Model):
	stopCode = models.IntegerField(default=0)
	latitude = models.FloatField(blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
