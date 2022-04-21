
# Django REST Framework
from rest_framework import serializers

# Models
from ..models import Post


class PostModelSerializer(serializers.ModelSerializer):

    class Meta:

        fields = '__all__'
        model = Post
