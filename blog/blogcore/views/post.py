

# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Models
from ..models import Post

# Serializers
from ..serializers.post import PostModelSerializer


class PostModelViewset(ModelViewSet):

    queryset = Post.objects.filter(status='P')
    serializer_class = PostModelSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            return super().get_permissions()
        return [AllowAny()]
