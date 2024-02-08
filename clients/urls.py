from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsListView, ClientCreateView

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientsListView.as_view(), name='clients_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
]
