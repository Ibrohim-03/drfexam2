from django.conf import settings
from django.db import models

class Channel(models.Model):
    TYPE_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='public')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='channels')
    created_at = models.DateTimeField(auto_now_add=True)

class Following(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'channel'], name='unique_following')
        ]