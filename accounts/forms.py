from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "sex")



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email",)

