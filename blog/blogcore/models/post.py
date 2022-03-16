

# Django
from django.db import models

# Models
from .category import Category
from .tag import Tag


STATUS_CHOICES = [
    ('P', 'Published'),
    ('D', 'Draft'),
]

DEFAULT_STATUS_CHOICE = 'P'

class Post(models.Model):

    title = models.CharField(max_length=50)
    body = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default=DEFAULT_STATUS_CHOICE
    )

    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='products')
    tag = models.ManyToManyField(Tag, verbose_name='tags')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    deleted_at = models.DateTimeField(auto_now=True, null=True, blank=True)
