from django.db import models


class ChatRoom(models.Model):
    TYPES = [(1, "Public"), (2, "Private")]

    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32, blank=True, null=True)
    type = models.IntegerField(choices=TYPES, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "ChatRoom"
        app_label = "duckchat"
