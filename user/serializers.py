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
    ValidationError  
    
)
from django.contrib.auth import get_user_model
from . import models
import django.contrib.auth.password_validation as validators

User = get_user_model()

#class TokenSerializer(serializers):
#    """
#    This serializer serializes the token data
#    """
#    token = serializers.CharField(max_length=255)

class RegisterSerializer(ModelSerializer):

    password = CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attr):
        validators.validate_password(attr['password'])
        return attr

    def create(self, validated_data):
        emailval = User.objects.filter(email=validated_data['email'])
        if emailval:
            raise ValidationError({'email': 'correct email adress'})
        account = User(
            email = validated_data['email'],
            username = validated_data['username']
        )

        password = validated_data['password']

        account.set_password(password)
        account.save()
        return account

class UserLoginSerializer(ModelSerializer):
    #token = CharField(allow_blank=True, read_only=True)
    username = CharField(max_length=255)
    password = CharField(max_length=255)
    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {'password':
                            {'write_only':True}
                            }
    def validate(self, data):
        return data

