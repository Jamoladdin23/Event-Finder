from django.urls import path
from registrations.views import RegistrationListCreate, RegistrationDetail

# from .views import RegistrationListCreate, RegistrationDetail


urlpatterns = [
    path('registrations/', RegistrationListCreate.as_view(), name='registration-list-create'),
    path('registrations/<int:pk>/', RegistrationDetail.as_view(), name='registration-detail'),
]