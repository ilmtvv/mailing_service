from django.urls import path
from users.apps import UsersConfig
from users.views import UserLoginView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login')
]