
# Django REST Framework
from rest_framework import serializers

from ..models import Category


class CategoryModelSerializer(serializers.ModelSerializer):

    slug = serializers.CharField(required=False)

    class Meta:

        fields = '__all__'
        model = Category

    def create(self, validated_data):

        return Category.objects.create(**validated_data, slug=validated_data['name'])
