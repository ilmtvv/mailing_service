from django.contrib.auth.forms import UserCreationForm

from django import forms
from users.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')