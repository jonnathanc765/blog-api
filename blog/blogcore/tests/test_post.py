
# Utils
from blog.blogcore.factories.tag import TagFactory
from blog.utils.api_test_cases import CustomAPITestCase

# Factories
from blog.blogcore.factories.post import PostFactory
from blog.blogcore.factories.category import CategoryFactory

# Django REST Framework
from rest_framework import status

# Models
from blog.blogcore.models import Post

class PostTest(CustomAPITestCase):

    TAG_NAME = 'React.js'

    def test_users_can_list_post(self):

        PostFactory.create_batch(20)

        response = self.client.get('/api/blog/posts/')

        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 20

        assert response.data[0]['body']
        assert response.data[0]['title']
        assert response.data[0]['created_at']
        assert response.data[0]['deleted_at'] == None

    def test_tags_list_is_returned_on_list(self):

        post = PostFactory.create()
        post.tags.add(TagFactory.create(name=self.TAG_NAME))

        response = self.client.get('/api/blog/posts/')

        assert len(response.data) == 1

        post = response.data[0]

        assert len(post['tags']) == 1

        for tag in post['tags']:
            assert tag == self.TAG_NAME

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

    def test_tags_list_is_returned_on_single(self):

        post = PostFactory.create()
        post.tags.add(TagFactory.create(name=self.TAG_NAME))

        response = self.client.get(f'/api/blog/posts/{post.id}/')

        post = response.data

        assert len(post['tags']) == 1

        for tag in post['tags']:
            assert tag == self.TAG_NAME

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

    def test_not_logged_users_cannot_create_posts(self):

        response = self.client.post("/api/blog/posts/", {
            'title': 'The best post',
            'body': 'The best body of post',
        })

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)
        assert  Post.objects.count() == 0

    def test_logged_users_can_create_posts(self):

        self._login()

        response = self.client.post("/api/blog/posts/", {
            'title': 'The best post',
            'body': 'The best body of post',
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        posts = Post.objects.all()
        assert posts.count() == 1
        assert posts.first().title == 'The best post'
        assert posts.first().body == 'The best body of post'
        assert posts.first().status == 'P'

    def test_users_can_set_category_on_create_post(self):

        self._login()

        category = CategoryFactory.create()

        response = self.client.post("/api/blog/posts/", {
            'title': 'The best post',
            'body': 'The best body of post',
            'category': category.pk
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

        assert Post.objects.count() == 1
        post = Post.objects.first()

        assert post.category != None
        assert post.category.pk == category.pk
        assert post.category.name == category.name

    def test_users_cannot_set_unexists_category_to_post(self):

        self._login()

        response = self.client.post("/api/blog/posts/", {
            'title': 'The best post',
            'body': 'The best body of post',
            'category': 999
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)

        assert Post.objects.count() == 0

    def test_users_can_set_posts_status_on_draft(self):

        self._login()

        response = self.client.post("/api/blog/posts/", {
            'title': 'The best post',
            'body': 'The best body of post',
            'status': 'D'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

        assert Post.objects.count() == 1
        assert Post.objects.first().status == 'D'

    def test_not_logged_users_cannot_update_posts(self):

        post = PostFactory.create()

        response = self.client.put(f"/api/blog/posts/{post.pk}/", {
            'title': 'The best post',
            'body': 'The best body of post',
        })

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED, response.data)

        assert post.title != 'The best post'
        assert post.body != 'The best body of post'

    def test_users_can_update_posts(self):

        self._login()

        post = PostFactory.create()

        response = self.client.put(f'/api/blog/posts/{post.pk}/', {
            'title': 'updated posts title',
            'body': 'updated posts body',
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = Post.objects.all()
        assert posts.count() == 1
        assert posts.first().title == 'updated posts title'
        assert posts.first().body == 'updated posts body'

    def test_users_can_update_category_on_post_too(self):

        self._login()

        category = CategoryFactory.create(name='New Category')

        post = PostFactory.create()

        response = self.client.put(f'/api/blog/posts/{post.pk}/', {
            'title': 'updated posts title',
            'body': 'updated posts body',
            'category': category.pk
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        posts = Post.objects.all()
        assert posts.count() == 1
        assert posts.first().title == 'updated posts title'
        assert posts.first().body == 'updated posts body'
        assert posts.first().category.pk == category.pk

    def test_users_can_update_status_on_draft(self):

        self._login()

        post = PostFactory.create()

        response = self.client.put(f'/api/blog/posts/{post.pk}/', {
            'title': 'updated posts title',
            'body': 'updated posts body',
            'status': 'D'
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        assert Post.objects.first().status == 'D'

    def test_users_can_destroy_posts(self):

        self._login()

        post = PostFactory.create()

        response = self.client.delete(f'/api/blog/posts/{post.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        assert Post.objects.count() == 0
