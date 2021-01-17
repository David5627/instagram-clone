from django.db import models
from cloudinary.models import  CloudinaryField
import cloudinary, cloudinary.api,cloudinary.uploader
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Following(models.Model):
    user= models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)


class InstaPhotos(models.Model):
    name = models.CharField(max_length = 20)
    image = CloudinaryField('image', null = True, blank = True)


