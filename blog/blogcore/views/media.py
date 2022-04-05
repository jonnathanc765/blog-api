

# Django REST Framework
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status

# Serializers
from blog.blogcore.serializers.media import MediaModelSerializer

# Models
from ..models import Media as MediaModel


class MediaModelViewset(
    GenericViewSet,
    CreateModelMixin
):

    serializer_class = MediaModelSerializer

    def get_queryset(self):
        return MediaModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(
            context={
                **self.get_serializer_context()
            },
            files=request.FILES['content']
        )
        serializer.is_valid(True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

