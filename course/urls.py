from django.urls import path
from .views import *

urlpatterns = [
    path('', GetAllCourseList.as_view()),
    path('topics/<int:id>/', GetTopics.as_view()),
    path('buycource/<int:id>/', BuyCource.as_view()),
    path('content/<int:id>/', GetContent.as_view()),
    path('api/v1/test/', TestViwes.as_view()),
]