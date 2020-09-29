from django.db import models


class Agent(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=64)
    zipcode = models.CharField(max_length=20)
    state = models.CharField(max_length=64)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)


class Places(models.Model):
    place_name = models.CharField(max_length=256)
    longitude = models.FloatField(blank=True)
    latitude = models.FloatField(blank=True)
