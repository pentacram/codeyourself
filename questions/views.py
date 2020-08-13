from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.status import *
from .models import *
from serializers import *
from user.models import *


class QuestionViews(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        users = request.user.profile

        if users:
            pass
        
        else:
            return JsonResponse({
                'status': HTTP_403_FORBIDDEN
            }, status=403)

