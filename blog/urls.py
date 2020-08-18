from django.urls import path
from .views import *

urlpatterns = [
    path('allblog', BlogList.as_view()),
    path('<int:id>/', MonoBlogList.as_view()),
]