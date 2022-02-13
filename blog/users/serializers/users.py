
# utils
from django.contrib.auth import get_user_model, authenticate, login

# Django REST Framework
from rest_framework import serializers


User = get_user_model


class SignInSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=16)

    def validate(self, attrs):
        user = authenticate(
            username=attrs['email'],
            password=attrs['password'],
        )
        if not user:
            raise serializers.ValidationError({'credentials': 'Email and password combination are not valid.'})

        user = self.context['user'] = user

        return attrs


    def save(self, **kwargs):

        request = self.context['view'].request
        user = self.context['user']
        login(request, user)
        return user

