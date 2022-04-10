
# Django
from django.db import models


AVAILABLE_EXTENSIONS = ['png', 'jpeg']
MAX_FILE_WEIGHT = 10240 # Kilobytes or 10 Megabytes

class Media(models.Model):

    content = models.FileField()
    created_at = models.DateTimeField(auto_now=True)
