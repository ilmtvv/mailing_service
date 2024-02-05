from django.urls import path
from users.apps import UsersConfig
from users.views import UserLoginView, RegisterView, succes, confirm, UserLogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('register/succes/', succes, name='succes'),
    path('register/<uuid:uuid>/', confirm, name='confirm'),
]