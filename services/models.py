from django.db import models

# Create your models here.

class DepartureTime(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    agencyName = models.CharField(max_length=100, blank=True, default='')
    routeName = models.CharField(max_length=100, blank=True, default='')
    stopName = models.CharField(max_length=100, blank=True, default='')
    stopCode = models.IntegerField(default=0)

    class Meta:
        ordering = ('created',)