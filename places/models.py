from django.db import models
from django.conf import settings


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
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_places"
    )
    photo_main = models.ImageField(upload_to="places", blank=True)
    photo_food = models.ImageField(upload_to="places", blank=True)
    photo_facilities = models.ImageField(upload_to="places", blank=True)
    photo_accommodation = models.ImageField(upload_to="places", blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
