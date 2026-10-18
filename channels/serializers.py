from rest_framework import serializers
from .models import Channel, Following

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'title', 'description', 'type', 'owner', 'created_at']
        read_only_fields = ['id', 'owner', 'created_at']

class FollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ['id', 'user', 'channel', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']