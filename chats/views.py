from rest_framework import viewsets, permissions, serializers
from django.db import models
from django.shortcuts import get_object_or_404
from .models import Chat
from .serializers import ChatSerializer
from accounts.models import Account

class ChatViewSet(viewsets.ModelViewSet):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(models.Q(user_1=user) | models.Q(user_2=user))

    def perform_create(self, serializer):
        user_2_id = self.request.data.get('user_2')
        user_2 = get_object_or_404(Account, id=user_2_id)
        if user_2 == self.request.user:
            raise serializers.ValidationError("Нельзя создать чат с самим собой.")
        
        existing_chat = Chat.objects.filter(
            models.Q(user_1=self.request.user, user_2=user_2) |
            models.Q(user_1=user_2, user_2=self.request.user)
        ).first()

        if existing_chat:
            return existing_chat
        
        serializer.save(user_1=self.request.user, user_2=user_2)