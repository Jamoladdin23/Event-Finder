from django.contrib.auth.models import User
from django.db import models
from events.models import Event


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username


class Booking(models.Model):
    event = models.ForeignKey(Event, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.event.title}'

