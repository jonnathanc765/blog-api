
# Utils
from typing import List

# Factory
import factory

# Models
from ..models import Category


class CategoryFactory(factory.django.DjangoModelFactory):

    name = factory.Faker('word')
    description = factory.Faker('word')
    slug = factory.Sequence(lambda n: n)

    class Meta:
        model = Category

    @classmethod
    def create(cls, **kwargs) -> Category:
        return super().create(**kwargs)

    @classmethod
    def create_batch(cls, size: int, **kwargs) -> List[Category]:
        return super().create_batch(size, **kwargs)



