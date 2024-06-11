from django.contrib.auth.models import User
from django.db import transaction
from events.models import Event
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .models import UserProfile, Booking
from .serializers import UserSerializer, UserProfileSerializer, BookingSerializer, UserDetailSerializer, \
    AdminUserUpdateSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserProfileDetail(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile


class BookingCreateView(generics.CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        event_id = request.data.get('events')
        user = request.user

        try:
            with transaction.atomic():
                # Lock the event row to ensure no concurrent updates
                event = Event.objects.select_for_update().get(id=event_id)

                if event.bookings.count == event.max_places:
                    return Response({'error': 'Participant limit reached for this event.'},
                                    status=status.HTTP_400_BAD_REQUEST)

                # Ensure a user cannot book the same event multiple times
                if Booking.objects.filter(event=event, user=user).exists():
                    return Response({'error': 'You have already booked this event.'},
                                    status=status.HTTP_400_BAD_REQUEST)

                # Increment the participant count and create the booking
                booking = Booking(event=event, user=user)
                booking.save()

                serializer = BookingSerializer(booking)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Event.DoesNotExist:
            return Response({'error': 'Event not found.'},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Catch all other exceptions and log them if needed
            return Response({'error': str(e)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdminUserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAdminUser]


class AdminUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserUpdateSerializer
    permission_classes = [IsAdminUser]
