from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username

class Avatar(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='avatars')
    image = models.FileField(upload_to='avatars/') 
    uploaded_at = models.DateTimeField(auto_now_add=True)