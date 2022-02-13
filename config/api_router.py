from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

urlpatterns = router.urls
urlpatterns += [
    # User management
    path("", include("blog.users.urls", namespace="users")),
]
