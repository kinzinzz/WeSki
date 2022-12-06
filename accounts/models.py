from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from places.models import Place

# Create your models here.
class User(AbstractUser):
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(300, 300)],
        format="JPEG",
        options={"quality": 90},
    )

    def profile_image(self):
        if self.image and hasattr(self.image, "url"):
            return self.image.url
        else:
            return "https://i.esdrop.com/d/f/bvRLlOwptP/D1wDSBrqJO.jpg"


# 결제 정보
class OrderTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    place = models.ForeignKey(
        Place, on_delete=models.PROTECT, related_name="order_places"
    )
    price = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    imp_uid = models.CharField(max_length=50)
    merchant_uid = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.id)
