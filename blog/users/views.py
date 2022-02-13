# Django
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status


# Serializers
from blog.users.serializers.users import SignInSerializer


User = get_user_model()


class AuthViewSet(viewsets.GenericViewSet):

    @action(mehtods=['POST'])
    def login(self, request, *args, **kwargs) -> Response:

        serializer = SignInSerializer(request.data)
        serializer.is_valid(True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
