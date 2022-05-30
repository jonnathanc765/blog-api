
# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Models
from ..models import Post

# Serializers
from ..serializers.post import PostModelSerializer, ReadPostSerializer


class PostModelViewset(ModelViewSet):

    serializer_class = PostModelSerializer

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return ReadPostSerializer
        return super().get_serializer_class()

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Post.objects.all()
        return Post.objects.filter(status='P')


    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            return super().get_permissions()
        return [AllowAny()]
