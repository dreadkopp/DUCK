from django.db import models
from duckchat.models.ChatRoom import ChatRoom
from duckchat.models.ChatUser import ChatUser


class Message(models.Model):
    message = models.CharField(max_length=128)
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(ChatUser, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(ChatUser, related_name='receiver', blank=True, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(ChatRoom, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ("timestamp",)
        app_label = "duckchat"
