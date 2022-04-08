
# Utils
import uuid
import os.path

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
        media = MediaModel(content=validated_data['content'])
        final_name = generate_uuid4_filename(media.content.name)
        media.content.name = final_name
        media.save()
        print(final_name)
        return media







def generate_uuid4_filename(filename):
    """
    Generates a uuid4 (random) filename, keeping file extension

    :param filename: Filename passed in. In the general case, this will
                     be provided by django-ckeditor's uploader.
    :return: Randomized filename in urn format.
    :rtype: str
    """
    discard, ext = os.path.splitext(filename)
    basename = f"{discard}-{uuid.uuid4().urn}"
    return f"{''.join(basename)}{ext}"
