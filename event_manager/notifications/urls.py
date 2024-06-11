from django.urls import path
from .views import NotificationList, mark_notification_as_read


urlpatterns = [
    path('notifications/', NotificationList.as_view(), name='notification-list'),
    path('notifications/<int:pk>/read/', mark_notification_as_read, name='mark-notification-as-read'),
]