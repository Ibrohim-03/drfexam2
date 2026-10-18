from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from .models import Post
from .serializers import PostSerializer
from channels.models import Channel

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        channel_id = self.kwargs.get('channel_id')
        if channel_id:
            return Post.objects.filter(channel_id=channel_id)
        return Post.objects.all()

    def perform_create(self, serializer):
        channel_id = self.kwargs.get('channel_id')
        channel = get_object_or_404(Channel, id=channel_id)
        if channel.owner != self.request.user:
            raise permissions.PermissionDenied("Публикации может создавать только владелец канала.")
        serializer.save(channel=channel)