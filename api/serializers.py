from rest_framework import serializers
from .models import PublicData, PrivateData, CustomUser

class PublicDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicData
        fields = ['id', 'content', 'created_at']

class PrivateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrivateData
        fields = ['id', 'content', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'telegram_username']