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

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class OneCourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name']

class TopicsSerializers(ModelSerializer):

        courses = OneCourseSerializers

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

    topicsname = TopicsSerializers()

    class Meta:
        model = Content
        fields = [
            'topicsname',
            'content',
        ]

class Main_TestSerializers(serializers.ModelSerializer):

    class Meta:
        model = Main_test
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

