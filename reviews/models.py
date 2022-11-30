from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from accounts.models import User
from places.models import Place
from django.conf import settings
# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=80)
    content=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    rating=models.PositiveIntegerField(null=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place=models.ForeignKey(Place, on_delete=models.CASCADE)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="likes_user")
    def __str__(self):
        return self.title
class ReviewImage(models.Model):
    review=models.ForeignKey(Review,on_delete=models.CASCADE)
    image = ProcessedImageField(
        blank=True,
        processors=[Thumbnail(300, 300)],
        format="JPEG",
        options={"quality": 90},
        upload_to="reviews/"
    )
