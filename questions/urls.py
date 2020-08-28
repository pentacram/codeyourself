from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    path('<int:id>', QuestionViews.as_view(), name='questions')
]