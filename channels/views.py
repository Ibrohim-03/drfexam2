from rest_framework import viewsets, permissions, filters, status
from rest_framework.response import Response
from django.db import models
from .models import Channel, Following
from .serializers import ChannelSerializer, FollowingSerializer

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['type']

    def get_queryset(self):
        return Channel.objects.filter(
            models.Q(type='public') | 
            models.Q(owner=self.request.user) | 
            models.Q(followers__user=self.request.user)
        ).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        channel = self.get_object()
        if channel.owner != request.user:
            return Response({"detail": "Только владелец может изменять канал."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)