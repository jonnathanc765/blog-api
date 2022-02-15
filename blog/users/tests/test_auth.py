
# Django
from django.contrib.auth import login

# Django REST Framwork
from rest_framework.test import APITestCase
from rest_framework import status

# Factories
from blog.users.factories.users import UserFactory


class AuthTest(APITestCase):

    def setUp(self) -> None:
        return super().setUp()


    def test_users_can_login_with_email_and_password(self):

        UserFactory.create(
            email='test@email.com'
        )

        response = self.client.post('/api/login/', {
            'email': 'test@email.com',
            'password': 'password' # Default password setted in factory
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)
        assert response.data != None
        assert isinstance(response.data, dict)
        assert 'user' in response.data
        assert 'access' in response.data
        assert 'refresh' in response.data
        assert 'test@email.com' == response.data['user']['email']

    def test_users_cannot_login_if_password_is_not_valid(self):

        UserFactory.create(
            email='test@email.com',
            password='testpassword'
        )

        response = self.client.post('/api/login/', {
            'email': 'test@email.com',
            'password': 'password'
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
        assert 'credentials' in response.data

    def test_users_can_logout(self):

        UserFactory.create(
            email='test@email.com',
        )

        response = self.client.post('/api/login/', {
            'email': 'test@email.com',
            'password': 'password' # Default password setted in factory
        })

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

        self.client.get('/api/logout/')

        response = self.client.get('/api/protected/')

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

