from django.db import models

from accounts.models import User
from auto_trade.models import Car


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    car = models.ForeignKey('auto_trade.Car', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)