from django.urls import path
from .views import UserProfileDetail, BookingCreateView


urlpatterns = [
    path('user/profile/', UserProfileDetail.as_view(), name='user-profile-detail'),
    path('bookings/', BookingCreateView.as_view(), name='booking-create'),
]