from django.db import models
from api.models import CustomUser

class TelegramUser(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='telegram')
    chat_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username or self.first_name} ({self.chat_id})"