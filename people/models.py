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


class Comment(models.Model):
    comment = models.CharField(max_length = 300)


class Profile(models.Model):
    bio = models.TextField(blank = True, null = True)
    dp = CloudinaryField('image', null = True, blank = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    following = models.ManyToManyField(Following)
    def save_profile(self):
        self.save()
    def delete_profile(self):
        Profile.objects.filter(id = self.id).delete()
    def update_profile(self, dp = None, bio = None):
        if dp is not None:
            Profile.objects.filter(id = self.id).update(dp = cloudinary.uploader.upload_resource(dp))
        if bio is not None:
            Profile.objects.filter(id = self.id).update(bio = bio)

    @classmethod
    def search_users(cls, search_term):
        users = [user for user in User.objects.all()]
        user = User.objects.filter(username__icontains = search_term).all()
        print(users)
        return user


