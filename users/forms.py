from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django import forms
from users.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()
