from rest_framework import serializers
from .models import Profile, Avatar

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'first_name', 'last_name', 'bio']
        read_only_fields = ['id']

class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['id', 'image', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']