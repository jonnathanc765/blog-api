
# Utils
from blog.utils.api_test_cases import CustomAPITestCase

# Factories
from blog.blogcore.factories.post import PostFactory

# Django REST Framework
from rest_framework import status

# Models
from blog.blogcore.models import Post

class PostTest(CustomAPITestCase):

    def test_users_can_list_post(self):

        PostFactory.create_batch(20)

        response = self.client.get('/api/blog/posts/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 20

        assert response.data[0]['body']
        assert response.data[0]['title']
        assert response.data[0]['created_at']

    def test_users_can_list_just_published_post(self):

        PostFactory.create_batch(20)
        PostFactory.create_batch(5, status='D')

        response = self.client.get('/api/blog/posts/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 20
