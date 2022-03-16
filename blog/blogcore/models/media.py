

from django.db import models


class Media(models.Model):

    content = models.FileField()
    created_at = models.DateTimeField(auto_now=True)
