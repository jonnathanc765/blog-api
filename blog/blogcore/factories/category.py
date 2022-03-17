
# Factory
import factory

# Models
from ..models import Category


class CategoryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('word')
    slug = factory.Faker('word')
