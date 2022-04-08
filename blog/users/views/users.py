# Django
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status

# Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

# Serializers
from blog.users.serializers.users import SignInSerializer


User = get_user_model()


class AuthViewSet(viewsets.GenericViewSet):

    authentication_classes = []
    permission_classes = [AllowAny]

    @action(methods=['POST', 'PUT'], detail=False)
    def login(self, request) -> Response:

        serializer = SignInSerializer(
            data=request.data,
            context={
                **self.get_serializer_context()
            }
        )
        serializer.is_valid(True)
        _, token_data = serializer.save()

        data = {
            'user': serializer.data,
            **token_data
        }

        return Response(data, status=status.HTTP_200_OK)

    @action(
        methods=['GET'],
        detail=False,
        permission_classes=[IsAuthenticated],
        authentication_classes=[JWTAuthentication]
    )
    def protected(self, request) -> Response:
        return Response('ok', status=status.HTTP_200_OK)
