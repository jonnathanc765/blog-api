
# Django
from django.urls import path, include

# Django REST Framework
from rest_framework import routers

# Views
from .views.categories import CategoryModelViewset
from .views.media import MediaModelViewset

router = routers.DefaultRouter()

router.register('categories', CategoryModelViewset, basename='categories')
router.register('media', MediaModelViewset, basename='media')

app_name = "blogcore"

urlpatterns = [
    path('', include(router.urls))
]
