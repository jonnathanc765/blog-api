

# Django REST Framework
from rest_framework import status

# TestCase
from blog.utils.api_test_cases import CustomAPITestCase

# Factories
from ..factories import CategoryFactory

# Models
from ..models import Category


class CategoryTest(CustomAPITestCase):

    def test_users_can_create_categories(self):

        self._login()

        response = self.client.post('/api/blog/categories/', {
            'name': 'Category test',
            'description': 'Description test'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        assert Category.objects.count() == 1
        assert Category.objects.first().name == 'Category test'
        assert Category.objects.first().description == 'Description test'

    def test_just_logged_in_users_can_create_categories(self):

        response = self.client.post('/api/blog/categories/', {
            'name': 'Category test',
            'description': 'Description test'
        })

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)

    def tests_users_can_create_category_with_parent(self):

        self._login()

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

        self._login()

        category = CategoryFactory.create()
        parent = CategoryFactory.create()

        response = self.client.put(f'/api/blog/categories/{category.id}/', {
            'name': 'Category test',
            'description': 'Description test',
            'parent': parent.id
        })

    def test_users_can_delete_categories(self):

        self._login()

        category = CategoryFactory.create()

        response = self.client.delete(f'/api/blog/categories/{category.id}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT, response.data)

        assert Category.objects.count() == 0

    def test_category_cannot_be_itself_parent(self):

        self._login()

        category = CategoryFactory.create()

        response = self.client.put(f'/api/blog/categories/{category.id}/', {
            'name': 'Category test',
            'description': 'Description test',
            'parent': category.id
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

        assert response.data['parent']

    def test_child_category_parent_field_is_setted_on_null_when_parent_is_deleted(self):

        self._login()

        parent = CategoryFactory.create()
        category = CategoryFactory.create(
            parent=parent
        )

        self.client.delete(f'/api/blog/categories/{parent.id}/')

        category.refresh_from_db()

        assert category.parent == None

    def test_name_is_required_when_category_will_be_created(self):

        self._login()

        response = self.client.post('/api/blog/categories/', {
            'description': 'Description test',
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

        assert response.data['name']

    def test_parent_categories_must_exists_when_create_a_category(self):

        self._login()

        response = self.client.post('/api/blog/categories/', {
            'name': 'Category test',
            'description': 'Description test',
            'parent': '-1' # This key never going to exists
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

        assert response.data['parent']
