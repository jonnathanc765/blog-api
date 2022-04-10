
# Utils
from typing import List

# Factory
import factory

# Models
from ..models import Media

# Django
from django.core.files.uploadedfile import SimpleUploadedFile


class MediaFactory(factory.django.DjangoModelFactory):

    content = SimpleUploadedFile("file.png", b"file_content", content_type="image/png")

    class Meta:
        model = Media

    @classmethod
    def create(cls, *_, **kwargs) -> Media:
        return super().create(**kwargs)

    @classmethod
    def create_batch(cls, size: int, *_, **kwargs) -> List[Media]:
        return super().create_batch(size, **kwargs)

