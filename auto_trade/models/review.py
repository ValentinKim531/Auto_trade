from django.db import models

from accounts.models import User
from auto_trade.models import Car


class Review(models.Model):
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    car = models.ForeignKey('auto_trade.Car', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
