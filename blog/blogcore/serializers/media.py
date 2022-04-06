
# Models
from ..models import Media as MediaModel, AVAILABLE_EXTENSIONS

# Django REST Framework
from rest_framework import serializers



class MediaModelSerializer(serializers.ModelSerializer):

    content = serializers.FileField(max_length=255)

    class Meta:

        model = MediaModel
        fields = ['content']

    def validate(self, attrs):
        content = attrs['content']
        ext = content.name.split('.')[-1]
        if not ext in AVAILABLE_EXTENSIONS:
            raise serializers.ValidationError({'content': 'Uploaded file is not accepted'})

        return attrs

    def create(self, validated_data):
        media = MediaModel.objects.create(
            content=validated_data['content']
        )
        return media
