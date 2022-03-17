

# Django REST Framework
from rest_framework.viewsets import ModelViewSet

# Models
from ..models import Category

# Serializers
from ..serializers.category import CategoryModelSerializer


class CategoryModelViewset(ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
