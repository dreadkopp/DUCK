from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class ChatUser(AbstractUser):
    pass

    ROLES = [(1, "Administrator"), (2, "Moderator"), (3, "Mitglied"), (4, "Gast")]

    nickname = models.CharField(max_length=16)
    role = models.IntegerField(choices=ROLES, default=4)
    icon = models.ImageField(upload_to='user_icons/', default='user_icons/no-img.png')
    id = models.AutoField(primary_key=True)

    objects = UserManager()
