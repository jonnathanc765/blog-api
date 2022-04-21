
# Utils
import factory
from typing import List

# Factories
from .category import CategoryFactory

# Models
from ..models import Post



class PostFactory(factory.django.DjangoModelFactory):

    title = factory.Faker('word')
    body = factory.Faker('word')
    category = factory.SubFactory(CategoryFactory)

    class Meta:
        model = Post

