from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from course.models import *

from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=155)
    surname = models.CharField(max_length=155)
    point = models.FloatField()
    image = models.ImageField(upload_to='photos/user')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}, {self.name}, {self.surname}, {self.point}"

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Profile.objects.create(user=instance)
   # instance.profile.save()

class UserCourse(models.Model):
    username = models.ForeignKey(Profile, on_delete=models.CASCADE)
    coursename = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}, {self.coursename}"
    