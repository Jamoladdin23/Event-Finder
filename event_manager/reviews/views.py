from django.utils import timezone
from rest_framework.response import Response
from rest_framework import generics, permissions, status

from events.permissions import IsOwnerOrReadOnly
from registrations.models import Registration

from .models import Review
from .serializers import ReviewSerializer


# Create your views here.
class ReviewListCreate(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        event = serializer.validated_data['event']
        if not Registration.objects.filter(user=self.request.user, event=event).exists():
            return Response({"error": "You can only review events you attended."}, status=status.HTTP_400_BAD_REQUEST)

        if event.date > timezone.now():
            return Response({"error": "You can only review events that have already occurred."},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save(user=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

