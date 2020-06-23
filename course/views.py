from django.shortcuts import render
from rest_framework.generics import *
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.status import *
from .models import *
from .serializers import *
from user.models import *

class GetAllCourseList(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = GetCourseSerializers

class GetCourseList(ListAPIView):
    serializer_class = GetCourseSerializers

    def get_queryset(self):
        ids = self.kwargs['id']
        return Course.objects.filter(pk=ids)

class BuyCource(APIView):
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
    serializer_class = GetTopicsSerializers

    def get_queryset(self):
        ids = self.kwargs['id']
        return Topics.objects.filter(courses__id=ids)
        

#def get_queryset(self):
#        ids = self.kwargs['id']
#        return EvSahibi.objects.filter(ev__id=ids)

class GetContent(APIView):
    
    serializer_class = GetContentSerializers

    def get_queryset(self):
        ids = self.kwargs['id']
        return Content.objects.filter(topicsname__id=ids)
    