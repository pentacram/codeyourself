from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer, BlogMonoSerializer
from django.http import JsonResponse
from rest_framework.status import *
from rest_framework.permissions import AllowAny
from django.core.paginator import Paginator

class BlogList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    paginate_by = 10


class MonoBlogList(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = BlogMonoSerializer
    paginate_by = 10

    def get_queryset(self):
        ids = self.kwargs['id']
        return Blog.objects.filter(id=ids)
                