from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    event = serializers.ReadOnlyField(source='event.title')

    class Meta:
        model = Review
        fields = ['id', 'user', 'event', 'rating', 'comment', 'created_at']
