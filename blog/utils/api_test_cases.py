
# Django
from rest_framework.test import APITestCase
from rest_framework import status

# Factories
from blog.users.factories.users import UserFactory

class CustomAPITestCase(APITestCase):

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
            HTTP_AUTHORIZATION=f"Bearer {response.data['access']}"
        )
        assert response.status_code == status.HTTP_200_OK
        return response.data
