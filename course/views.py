from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.generics import *
from rest_framework.views import APIView
from django.http import JsonResponse
from django.core.paginator import Paginator
from rest_framework.status import *
from .models import *
from .serializers import *
from user.models import *

class GetAllCourseList(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    paginate_by = 10


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
    permission_classes = [AllowAny]
    serializer_class = TopicsSerializers
    paginate_by = 10

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


class TestViwes(APIView):
    def get(self,request,format=None):
        if self.request.GET.get('main_id'):
            task = Test.objects.filter(main_id=self.request.GET.get('main_id'))
            serializer = TestSerializers(task, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'topic secin'})

    def post(self,request,format=None):
        try:
            if request.data['user']:
                get_test = Test.objects.get(id=request.data['t_id'])
                a = get_test.check_answer(request.data['variant'], request.data['user'])
                return Response({'data':a})
        except:
            return Response({'error':'Duzgun melumat gonderilmedi'})
    