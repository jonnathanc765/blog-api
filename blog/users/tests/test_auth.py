

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
            'email': 'test@email.com'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert response.data != None
