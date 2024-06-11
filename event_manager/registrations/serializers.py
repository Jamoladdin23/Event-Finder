from rest_framework import serializers
from .models import Registration


class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    event = serializers.ReadOnlyField(source='event.title')

    class Meta:
        model = Registration
        fields = ['id', 'user', 'event', 'registered_at']


