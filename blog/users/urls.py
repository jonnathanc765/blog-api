
# Django
from django.urls import path, include

# Django REST Framework
from rest_framework import routers

# Views
from blog.users.views import AuthViewSet

app_name = "users"

router = routers.DefaultRouter()
router.register(r'', AuthViewSet, basename='users')


urlpatterns = [
    path('', include(router.urls))
]
