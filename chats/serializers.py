from rest_framework import serializers
from .models import Chat

class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ['id', 'user_1', 'user_2', 'created_at']
        read_only_fields = ['id', 'user_1', 'created_at']