from .models import *
from rest_framework.serializers import ModelSerializer, RelatedField, SlugRelatedField


class QuestionSerializer(ModelSerializer):
    answers = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='answer'
     )

    class Meta:
        model = Questions
        fields = ['question', 'answers']