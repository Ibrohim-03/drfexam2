from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'channel', 'title', 'description', 'content', 'created_at']
        read_only_fields = ['id', 'channel', 'created_at']