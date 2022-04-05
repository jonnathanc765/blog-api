from django.test.client import BOUNDARY, MULTIPART_CONTENT, encode_multipart
# Django
from rest_framework.test import APITestCase
from rest_framework import status

from django.core.files.uploadedfile import SimpleUploadedFile

# Models
from blog.blogcore.models import Media

class MediaTest(APITestCase):

    tmp_file = SimpleUploadedFile(
        "image.jpg",
        "file_content",
        content_type="image/jpg"
    )

    def test_users_can_upload_images(self):

        with open(self.tmp_file, 'rb') as image:

            response = self.client.post(
                '/api/blog/media/',
                encode_multipart(
                    BOUNDARY,
                    {
                        'content': image
                    }
                ),
                content_type=MULTIPART_CONTENT
            )

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        assert Media.objects.count() == 1
        assert Media.objects.first().content
