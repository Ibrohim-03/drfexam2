from django.urls import path
from .views import MessageViewSet

urlpatterns = [
    path('<int:chat_id>/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='chat-messages'),
]