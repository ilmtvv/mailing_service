from django.shortcuts import render
from django.contrib.auth.views import LoginView
from users.forms import UserForm

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserForm
