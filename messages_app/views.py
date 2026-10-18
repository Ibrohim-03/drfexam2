from rest_framework import viewsets, permissions, serializers
from django.shortcuts import get_object_or_404
from .models import Message
from .serializers import MessageSerializer
from chats.models import Chat

class MessageViewSet(viewsets.ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs.get('chat_id')
        chat = get_object_or_404(Chat, id=chat_id)
        if self.request.user not in [chat.user_1, chat.user_2]:
            return Message.objects.none()
        return Message.objects.filter(chat=chat)

    def perform_create(self, serializer):
        chat_id = self.kwargs.get('chat_id')
        chat = get_object_or_404(Chat, id=chat_id)
        if self.request.user not in [chat.user_1, chat.user_2]:
            raise serializers.ValidationError("Вы не участник этого чата.")
        serializer.save(sender=self.request.user, chat=chat)