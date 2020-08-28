from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.status import *
from .models import *
from .serializers import *
from user.models import *
from django.core.paginator import Paginator


class QuestionViews(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    paginate_by = 1

    def get(self, *args, **kwargs):
        #users = request.user.profile

        #if users:
            #query = Questions.objects.filter(content.id = request.GET.get('id')).first()
        pk = kwargs.get("id")
        question = Questions.objects.filter(content__id=pk).first()
        print('dhsdhcjkdhjhvkhjhjvhv',question)
        return JsonResponse({
            'data': question
        })