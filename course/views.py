from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.generics import *
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.status import *
from .models import *
from .serializers import *
from user.models import *

class GetAllCourseList(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = GetCourseSerializers

class GetCourseList(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetCourseSerializers

    def get_queryset(self):
        ids = self.kwargs['id']
        return Course.objects.filter(pk=ids)

class BuyCource(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BuyCourseSerializers

    def post(self, request, *args, **kwargs):
        pk = kwargs.get('id')
        users = request.user.profile
        course = Course.objects.filter(pk=pk).first()
        if users and course:
            cour = UserCourse(
                username=users,
                coursename = course.name
            )
            cour.save()
            return JsonResponse({
                'status': HTTP_201_CREATED,
                'data': cour
            })
        else:
            return JsonResponse({
                'status': HTTP_400_BAD_REQUEST
            }, status=400)


class GetTopics(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetTopicsSerializers

    def get_queryset(self):
        ids = self.kwargs['id']
        data = Topics.objects.filter(courses__id=ids)
        return data
        

class GetContent(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GetContentSerializers

    def get_queryset(self):
        ids = self.kwargs['id']
        return Content.objects.filter(topicsname__id=ids)
    