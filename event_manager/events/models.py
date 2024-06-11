from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    date = models.DateTimeField()
    max_places = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, related_name='events', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}, {self.location}, {self.date}, {self.max_places}"




