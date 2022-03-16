
# Django
from django.db import models

class Category(models.Model):

    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ['name']
