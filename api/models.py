from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telegram_username = models.CharField(max_length=100, blank=True, null=True)

class PublicData(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PrivateData(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)