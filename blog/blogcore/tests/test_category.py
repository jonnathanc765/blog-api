
# Django
from rest_framework.test import APITestCase

# Django REST Framework
from rest_framework import status

# Factories
from ..factories import CategoryFactory

# Models
from ..models import Category


class CategoryTest(APITestCase):

    def test_users_can_create_categories(self):

        response = self.client.post('/api/blog/categories/', {
            'name': 'Category test',
            'description': 'Description test'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        assert Category.objects.count() == 1
        assert Category.objects.first().name == 'Category test'
        assert Category.objects.first().description == 'Description test'

    def tests_users_can_create_category_with_parent(self):

        parent = CategoryFactory.create()

        response = self.client.post('/api/blog/categories/', {
            'name': 'Category test',
            'description': 'Description test',
            'parent': parent.pk
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        assert Category.objects.count() == 2
        assert Category.objects.exclude(pk=parent.pk).first().parent.pk == parent.pk
