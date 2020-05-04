from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
from django.http import JsonResponse
from rest_framework.status import *

class BlogList(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class MonoBlogList(ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        ids = self.kwargs['id']
        return Blog.objects.filter(id=ids)
