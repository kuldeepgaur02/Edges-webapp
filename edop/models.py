from django.db import models

# Create your models here.
class Pictiure(models.Model):
    venue_image=models.ImageField(null=True,blank=True,upload_to="images/")