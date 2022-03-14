
# Django
from django.contrib.auth import login

# Django REST Framwork
from rest_framework.test import APITestCase
from rest_framework import status

# Factories
from blog.users.factories.users import UserFactory


class AuthTest(APITestCase):

    email = 'test@email.com'
    password = 'password' # Default password setted in factory

    def _login(self):

        UserFactory.create(
            email=self.email
        )
        response = self.client.post('/api/login/', {
            'email': self.email,
            'password': self.password
        })
        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer %s' % response.data['access'])
        assert response.status_code == status.HTTP_200_OK
        return response.data


    def test_users_can_login_with_email_and_password(self):

        UserFactory.create(
            email=self.email
        )

        response = self.client.post('/api/login/', {
            'email': self.email,
            'password': self.password
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

    def test_guest_users_cannot_access_protected_page(self):

        response = self.client.get('/api/protected/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_users_can_use_access_token_to_access_to_protected_page(self):

        self._login()

        response2 = self.client.get('/api/protected/')

        self.assertEqual(response2.status_code, status.HTTP_200_OK)
        assert response2.data


    # def test_users_can_logout(self):

    #     UserFactory.create(
    #         email='test@email.com',
    #     )

    #     response = self.client.post('/api/login/', {
    #         'email': 'test@email.com',
    #         'password': 'password' # Default password setted in factory
    #     })

    #     self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + response.data['access'])

    #     self.client.get('/api/logout/')

    #     response2 = self.client.get('/api/protected/')

    #     self.assertEqual(response2.status_code, status.HTTP_403_FORBIDDEN)

