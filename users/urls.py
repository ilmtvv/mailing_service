from django.urls import path
from users.apps import UsersConfig
from users.views import UserLoginView, RegisterView, succes, confirm, UserLogoutView, UserUpdateView, UserAllView, \
    checkout_status

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),

    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('all/', UserAllView.as_view(), name='all'),
    path('all/status/<int:pk>/', checkout_status, name='checkout-status'),

    path('register/succes/', succes, name='succes'),
    path('register/<uuid:uuid>/', confirm, name='confirm'),
]