from django.urls import path
from .views import PostViewSet

urlpatterns = [
    path('post', PostViewSet.as_view({'get': 'list'}), name='post-list'),
    path('<int:pk>/', PostViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy'}), name='post-detail'),
    path('channel/<int:channel_id>/', PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='channel-posts'),
]