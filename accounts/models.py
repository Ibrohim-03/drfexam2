from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class Account(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, blank=True, null=True)
