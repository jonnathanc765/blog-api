
# Utils
from blog.utils.api_test_cases import CustomAPITestCase

# Django
from django.test.client import BOUNDARY, MULTIPART_CONTENT, encode_multipart
from django.core.files.uploadedfile import SimpleUploadedFile

# Django REST Framework
from rest_framework import status

# Models
from blog.blogcore.models import Media, AVAILABLE_EXTENSIONS

class MediaTest(CustomAPITestCase):

    def generate_photo_file(self, extension):
        return SimpleUploadedFile(f"file.{extension}", b"file_content", content_type="image/{extension}")

    def test_users_can_upload_images(self):

        self._login()

        for extension in AVAILABLE_EXTENSIONS:
            response = self.client.post(
                '/api/blog/media/',
                encode_multipart(
                    BOUNDARY,
                    {
                        'content': self.generate_photo_file(extension)
                    }
                ),
                content_type=MULTIPART_CONTENT
            )

            self.assertEqual(status.HTTP_201_CREATED, response.status_code, response.data)

        assert Media.objects.count() == len(AVAILABLE_EXTENSIONS)

    def test_users_cannot_create_media_objects_with_no_accepted_files_extension(self):

        self._login()

        for extension in ['bmp']:
            response = self.client.post(
                '/api/blog/media/',
                encode_multipart(
                    BOUNDARY,
                    {
                        'content': SimpleUploadedFile("file.mp4", b"file_content", content_type="video/mp4")
                    }
                ),
                content_type=MULTIPART_CONTENT
            )
            self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
            assert 'content'  in response.data

        assert Media.objects.count() == 0
