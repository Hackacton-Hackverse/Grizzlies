from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Conversation(models.Model):
    participants = models.ManyToManyField(User)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
