from django.db import models
from django.contrib.auth.models import User  # Import the User model from the appropriate module

from item.models import Item

# Create your models here.
class Conversation(models.Model):
    item = models.ForeignKey(Item, related_name="conversations", on_delete=models.CASCADE)  # A conversation belongs to an item
    members = models.ManyToManyField(User, related_name="conversations")  
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the field to now when the object is first created.
    modified_at = models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is saved.

    class Meta:
        ordering = ("-modified_at",)
    

class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="created_messages", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)