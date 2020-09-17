from rest_framework import serializers
from . import models

class BlogMonoSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = ('id', 'title', 'article', 'image', 'created_at', 'updated_at')

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = ['id', 'image', 'title', 'article']


        