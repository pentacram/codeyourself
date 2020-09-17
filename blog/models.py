from django.db import models
from ckeditor.fields import RichTextField

class Blog(models.Model):
    title = models.TextField()
    article = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.article}"
