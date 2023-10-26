from django.db import models

from accounts.models import User


class Message(models.Model):
    sender = models.ForeignKey('accounts.User', related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey('accounts.User', related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
