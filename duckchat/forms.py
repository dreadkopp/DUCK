from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import ChatUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ChatUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = ChatUser
        fields = UserChangeForm.Meta.fields
