from django.db import models
from django.utils import timezone
import datetime
from django.utils.text import slugify
from fotowebapp import utils as U

# Create your models here.
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    type = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.group_name

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    type = models.PositiveSmallIntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    latest_access = models.DateField()

    def __str__(self):
        return self.user_name
    
class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=100) 
    customer_name = models.CharField(max_length=100)
    cover_photo = models.CharField(max_length=100)
    allow_comment = models.BooleanField()
    allow_download = models.BooleanField()
    nb_of_selected_photo = models.PositiveSmallIntegerField()
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    expired_date = models.DateField()
    is_created_by_group = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_shared = models.BooleanField()
    drive_link = models.URLField()

    def __str__(self):
        return self.album_name

class ShareInfo(models.Model):
    share_id = models.AutoField(primary_key=True)
    share_link = models.URLField()
    is_public = models.BooleanField()
    expired_date = models.DateField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    is_shared_with_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Image(models.Model):
    image_id = models.AutoField(primary_key=True)
    image_metadata_id = models.CharField(max_length=100)
    image_name = models.CharField(max_length=50)
    created_date = models.DateField(default=timezone.now)
    modified_date = models.DateField()
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    comment = models.CharField(max_length=200, blank=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.image_name