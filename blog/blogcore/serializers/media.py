
# Models
from ..models import Media as MediaModel

# Django REST Framework
from rest_framework import serializers



class MediaModelSerializer(serializers.ModelSerializer):

    content = serializers.FileField(max_length=255, allow_empty_file=False)

    def create(self, validated_data):

        pass
