
# Django
from django.urls import path, include

# Django REST Framework
from rest_framework import routers

# Views
from .views.categories import CategoryModelViewset

router = routers.DefaultRouter()

router.register('categories', CategoryModelViewset, basename='categories')

app_name = "blogcore"

urlpatterns = [
    path('', include(router.urls))
]
