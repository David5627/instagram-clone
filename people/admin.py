from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(InstaPhotos)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(Following)

