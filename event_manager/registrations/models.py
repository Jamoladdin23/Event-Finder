from django.contrib.auth.models import User
from django.db import models
from events.models import Event


class Registration(models.Model):
    user = models.ForeignKey(User, related_name='registrations', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='registrations', on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
