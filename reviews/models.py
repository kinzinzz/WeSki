from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from places.models import Place
from django.conf import settings
from urllib.parse import unquote
import os
# Create your models here.
class Review(models.Model):
    title=models.CharField(max_length=80)
    content=models.TextField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    rating=models.PositiveIntegerField(null=True,)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place=models.ForeignKey(Place, on_delete=models.CASCADE)
    likes=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="like_Review")
    likes_num=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
class ReviewImage(models.Model):
    review=models.ForeignKey(Review,on_delete=models.CASCADE)
    image = ProcessedImageField(
        processors=[Thumbnail(300, 300)],
        format="JPEG",
        options={"quality": 90},
        upload_to="reviews/"
    )
    def delete(self,*args,**kargs):
        if self.image:
            temp=unquote(self.image.path)
            temp0=os.path.join(str(settings.MEDIA_ROOT),temp)
            if os.path.isfile(temp0):
                os.remove(temp0)
            super(ReviewImage, self).delete(*args, **kargs)
