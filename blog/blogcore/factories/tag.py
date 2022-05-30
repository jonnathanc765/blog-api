
# Utils
from typing import List

# Factory
import factory

# Models
from ..models import Tag


class TagFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('word')

    class Meta:
        model = Tag

    @classmethod
    def create(cls, **kwargs) -> Tag:
        return super().create(**kwargs)

    @classmethod
    def create_batch(cls, size: int, **kwargs) -> List[Tag]:
        return super().create_batch(size, **kwargs)



