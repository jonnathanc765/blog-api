
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

    def tests_users_can_retrieve_categories(self):

        CategoryFactory.create_batch(20)

        response = self.client.get('/api/blog/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        assert len(response.data) == 20

    def test_users_can_retrieve_single_categories(self):

        category = CategoryFactory.create(
            name='Category test',
            description='Description test'
        )

        response = self.client.get(f'/api/blog/categories/{category.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        assert response.data
        assert response.data['name'] == 'Category test'
        assert response.data['description'] == 'Description test'

    def test_users_can_update_categories(self):

        category = CategoryFactory.create()
        parent = CategoryFactory.create()

        response = self.client.put(f'/api/blog/categories/{category.id}/', {
            'name': 'Category test',
            'description': 'Description test',
            'parent': parent.id
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

        assert response.data['name'] == 'Category test'
        assert response.data['description'] == 'Description test'
        assert response.data['parent'] == parent.id
