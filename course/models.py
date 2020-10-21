from django.db import models
from user.models import User
from rest_framework.response import Response
from django.http import JsonResponse

class Course(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/course')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Topics(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    status_list = (
        ('public', 'public'),
        ('private', 'private'),
    )
    status = models.CharField(max_length=255, choices=status_list, null=True, blank=True)

class Content(models.Model):
    topicsname = models.ForeignKey(Topics, on_delete=models.CASCADE)
    content = models.TextField()
    point = models.PositiveIntegerField(default=0)


class Main_test(models.Model):
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE, related_name='test')
    

class Test(models.Model):
    main = models.ForeignKey(Main_Test, on_delete=models.CASCADE)
    name = models.TextField()
    point = models.PositiveIntegerField(default=50)
    correct_answer = models.CharField(max_length=5)

    def check_answer(self, answer, user=None):
        if self.correct_answer == answer:
            user = User.objects.get(id=user)
            user.point += self.point
            user.save()
            data = 'Duzgun Cavab verildi!'
            return data
        else:
            data = 'Sehf cavab verildi!'
            return data



class Question(models.Model):
    test = models.ForeignKey(Test,on_delete=models.CASCADE,related_name='quest_test')
    variant = models.CharField(max_length=10)
    #t_id = models.PositiveIntegerField(default=0)
    question = models.CharField(max_length=200)
    

