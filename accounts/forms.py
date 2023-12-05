from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ("username", "email")

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("email", "last_name")

