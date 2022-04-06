
# Django
from django.db import models


AVAILABLE_EXTENSIONS = ['png', 'jpge']

class Media(models.Model):

    content = models.FileField()
    created_at = models.DateTimeField(auto_now=True)
