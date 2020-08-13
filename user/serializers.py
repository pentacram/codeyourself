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
from django.contrib.auth.models import User
from . import models

#class TokenSerializer(serializers):
#    """
#    This serializer serializes the token data
#    """
#    token = serializers.CharField(max_length=255)

class RegisterSerializer(ModelSerializer):

    password2 = CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        emailval = User.objects.filter(email=self.validated_data['email'])
        if emailval:
            raise ValidationError({'email': 'correct email adress'})
        account = User(
            email = self.validated_data['email'],
            username = self.validated_data['username']
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise ValidationError({'password': 'Passwords must match'})

        account.set_password(password)
        account.save()
        return account

