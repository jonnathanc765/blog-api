"""
    test
"""

# Django
from django.conf import settings
from django.urls import path, include

# Django REST Framwork
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt import views as jwt_views

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

urlpatterns = router.urls
urlpatterns += [
    # User management
    path("", include("blog.users.urls", namespace="users")),
    path("blog/", include("blog.blogcore.urls", namespace="blog")),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
