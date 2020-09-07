from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer, BlogMonoSerializer
from django.http import JsonResponse
from rest_framework.status import *
from rest_framework.permissions import AllowAny

class BlogList(ListAPIView):
    queryset = Blog.objects.all()
    permission_classes = [AllowAny]
    serializer_class = BlogSerializer


class MonoBlogList(ListAPIView):
    serializer_class = BlogMonoSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        ids = self.kwargs['id']
        return Blog.objects.filter(id=ids)
                