from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    opening_time = models.CharField(max_length=80)
    break_day = models.CharField(max_length=80)
    contact_number = models.CharField(max_length=80)
    subtext = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hits = models.IntegerField(default=0)
    price = models.PositiveIntegerField(default=0, null=True)
    # latitude = models.FloatField()
    # longtitude = models.FloatField()
