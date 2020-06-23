from django.db import models

class Blog(models.Model):
    title = models.TextField()
    article = models.TextField()
    image = models.ImageField(upload_to='photos/blog')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}, {self.article}"
