from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_jwt.settings import api_settings
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from rest_framework.generics import *
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from .serializers import *
import json
from django.http import JsonResponse
from rest_framework.status import *


class CreateUserView(CreateAPIView):
    model = User.objects.all()
    serializer_class = RegisterSerializer

