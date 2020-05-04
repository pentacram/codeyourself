from rest_framework import serializers
from . import models

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'article', 'image', 'created_at', 'updated_at',)
        model = models.Blog