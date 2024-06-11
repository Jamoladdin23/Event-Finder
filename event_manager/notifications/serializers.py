from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Notification
        fields = ['id', 'user', 'message', 'is_read', 'created_at']