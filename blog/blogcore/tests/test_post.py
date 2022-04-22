
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

    def test_users_can_retrieve_single_posts(self):

        post = PostFactory.create()

        response = self.client.get(f"/api/blog/posts/{post.pk}/")

        assert response.status_code == 200
        assert response.data['title'] == post.title
        assert response.data['body'] == post.body

    def test_users_can_retrieve_just_published_posts(self):

        post = PostFactory.create(status='D')

        response = self.client.get(f"/api/blog/posts/{post.pk}/")

        assert response.status_code == 404

    def test_logged_users_can_retrieve_draft_post(self):

        self._login()

        post = PostFactory.create(status='D')

        response = self.client.get(f"/api/blog/posts/{post.pk}/")

        assert response.status_code == 200
        assert response.data['title'] == post.title
        assert response.data['body'] == post.body

    def test_logged_users_can_create_posts(self):

        self._login()

        response = self.client.get(f"/api/blog/posts/", {
            'title': 'The best post',
            'body': 'The best body of post',
        })
