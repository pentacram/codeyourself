from django.db import models
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
#from django.contrib.auth.models import User
from course.models import *
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    fullname = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, unique=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    point = models.PositiveIntegerField(default=0)
    level = models.PositiveIntegerField(default=0)
    img =  models.ImageField(blank=True,null=True)

    def save(self,*args,**kwargs):
        if self.point >= 50:
            self.level= 1
        if self .point >= 200:
            self.level = 2
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
 #   if created:
  #      Profile.objects.create(user=instance)
   # instance.profile.save()


class Badge(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    badge = models.PositiveIntegerField(default=0)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True,null=True)


    def __str__(self):
        return user.username


class UserCourse(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    coursename = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}, {self.coursename}"

class UserTopic(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    topicName = models.ForeignKey(Topics,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    

class UserContent(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ContentName = models.ForeignKey(Content,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class UserTest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    test = models.ForeignKey(Test,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
