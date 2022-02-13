
# Utils
import factory

# Django
from django.contrib.auth.hashers import make_password

# models
from blog.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    password = factory.LazyFunction(lambda: make_password('password'))

    class Meta:
        model = User
