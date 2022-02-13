
# utils
from django.contrib.auth import get_user_model, authenticate, login

# Django REST Framework
from rest_framework import serializers


User = get_user_model


class SignInSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=16)


    def save(self, **kwargs):

        validated_data = {**self.validated_data, **kwargs}

        request = self.context['view'].request

        user = authenticate(
            request,
            username=validated_data['email'],
            password=validated_data['password'],
        )

        if user:
            login(request, user)

        return user

