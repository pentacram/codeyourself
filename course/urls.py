from django.urls import path
from .views import *
from rest_framework import routers

urlpatterns = [
    path('', GetAllCourseList.as_view()),
    path('<int:id>/', GetOneCourse.as_view()),
    path('buycource/<int:id>/', BuyCource.as_view()),
    path('content/<int:id>/', GetContent.as_view()),
    path('api/v1/test/', TestViwes.as_view()),
]