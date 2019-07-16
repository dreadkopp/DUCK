from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from duckchat.models.ChatRoom import ChatRoom
from duckchat.models.Message import Message
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import ChatUser


class CustomUserAdmin(UserAdmin):
    model = ChatUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('icon', 'role', 'nickname')}),
    )


# Register your models here.
admin.site.register(ChatRoom)
admin.site.register(Message)
admin.site.register(ChatUser, CustomUserAdmin)
