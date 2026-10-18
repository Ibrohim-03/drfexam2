from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet, AvatarViewSet

router = DefaultRouter()
router.register(r'avatars', AvatarViewSet, basename='avatar')
router.register(r'', ProfileViewSet, basename='profile')

urlpatterns = [
    path('', include(router.urls)),
]