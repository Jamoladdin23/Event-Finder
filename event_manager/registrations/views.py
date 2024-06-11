from rest_framework import generics, permissions, status
from rest_framework.response import Response
from notifications.models import Notification

from .models import Registration
from .serializers import RegistrationSerializer


class RegistrationListCreate(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        user_profile = self.request.user.userprofile

        if event.current_participants >= event.max_places:
            return Response({"error": "Event is fully booked."}, status=status.HTTP_400_BAD_REQUEST)

        if user_profile.balance < event.price:
            return Response({"error": "Insufficient balance."}, status=status.HTTP_400_BAD_REQUEST)

        event.current_participants += 1
        event.save()

        user_profile.balance -= event.price
        user_profile.save()

        serializer.save(user=self.request.user)
        Notification.objects.create(
            user=self.request.user,
            message=f'You have successfully registered for the event: {event.title}'
        )


class RegistrationDetail(generics.RetrieveDestroyAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        event = instance.event
        user_profile = instance.user.userprofile

        event.current_participants -= 1
        event.save()

        user_profile.balance += event.price
        user_profile.save()

        Notification.objects.create(
            user=instance.user,
            message=f'Your registration for the event: {event.title} has been cancelled'
        )

        instance.delete()
# Create your views here.
