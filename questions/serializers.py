from .models import *
from rest_framework.serializers import ModelSerializer, RelatedField, SlugRelatedField


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['answer', 'is_answer']

class QuestionSerializer(ModelSerializer):
    answers = AnswerSerializer

    class Meta:
        model = Questions
        fields = ['question', 'answers']