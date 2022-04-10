
# Utils
import uuid
import os.path

# Models
from ..models import Media as MediaModel, AVAILABLE_EXTENSIONS, MAX_FILE_WEIGHT

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
        if content.size > MAX_FILE_WEIGHT:
            max_weight_kb = str(MAX_FILE_WEIGHT)
            raise serializers.ValidationError({'content': "File weight cannot be more than {} Kilobytes".format(max_weight_kb)})

        return attrs

    def create(self, validated_data):
        media = MediaModel(content=validated_data['content'])
        final_name = generate_uuid4_filename(media.content.name)
        media.content.name = final_name
        media.save()
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
    basename = f"{discard}-{str(uuid.uuid4())}"
    return f"{''.join(basename)}{ext}"
