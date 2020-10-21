from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from rest_framework.serializers import (
    CharField,
    EmailField,
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
    ChoiceField,
    DateField,
    StringRelatedField,
    DictField,    
)
from django.core import serializers
import json
from django.http import JsonResponse
from .models import *
from user.models import *


User = get_user_model()

class GetCourseSerializers(ModelSerializer):
    
    class Meta:
        model = Course
        fields = ['name', 'photo', 'created_at', 'updated_at']

class GetTopicsSerializers(ModelSerializer):

        courses = GetCourseSerializers()

        class Meta:
            model = Topics
            fields = [
                'courses',
                'name',
            ]

class BuyCourseSerializers(ModelSerializer):

    class Meta:
        model = UserCourse
        fields = [
            'username',
            'coursename'
        ]

class GetContentSerializers(ModelSerializer):

    topicsname = GetTopicsSerializers()

    class Meta:
        model = Content
        fields = [
            'topicsname',
            'content',
        ]

class Main_TestSerializers(serializers.ModelSerializer):

    class Meta:
        model = Main_Test
        fields = '__all__'

class QuestionSerializers(serializers.ModelSerializer):
    #test = TestSerializers(read_only=True)
    class Meta:
        model = Question
        fields = '__all__'

class TestSerializers(serializers.ModelSerializer):
    #main = Main_TestSerializers(read_only=True)
    quest_test = QuestionSerializers(many=True)
    class Meta:
        model = Test
        exclude = ['correct_answer',]

