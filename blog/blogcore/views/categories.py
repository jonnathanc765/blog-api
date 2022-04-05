

# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

# Models
from ..models import Category

# Serializers
from ..serializers.category import CategoryModelSerializer


class CategoryModelViewset(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'delete']:
            return super().get_permissions()
        return [AllowAny()]
