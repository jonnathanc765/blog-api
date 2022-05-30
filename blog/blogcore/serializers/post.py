
# Django REST Framework
from rest_framework import serializers

# Models
from ..models import Post


class PostModelSerializer(serializers.ModelSerializer):

    class Meta:

        fields = '__all__'
        model = Post


class ReadPostSerializer(PostModelSerializer):

    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
