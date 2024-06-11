from django.contrib.auth.models import User
from django.db import models
from events.models import Event


class Review(models.Model):
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    event = models.ForeignKey(Event, related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')


