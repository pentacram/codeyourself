from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogList.as_view()),
    path('<int:id>/', MonoBlogList.as_view()),
]