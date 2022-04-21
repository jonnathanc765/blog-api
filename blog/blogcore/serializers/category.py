
# Utils
from typing import Any

# Django REST Framework
from rest_framework import serializers

# Models
from ..models import Category


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:

        fields = '__all__'
        model = Category

    def validate(self, attrs: Any) -> Any:
        if self.instance:
            if attrs.get('parent', None):
                if getattr(self.instance, 'pk', None) == attrs['parent'].pk:
                    raise serializers.ValidationError({'parent': 'parent cannot be itself category'})

        return attrs

    def create(self, validated_data):

        return Category.objects.create(**validated_data, slug=validated_data['name'])
