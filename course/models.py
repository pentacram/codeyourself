from django.db import models

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
    

