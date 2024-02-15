from django.urls import path

from clients.apps import ClientsConfig
from clients.views import ClientsListView, ClientCreateView, ClientUpdateView, DeleteClientView, delete_client

app_name = ClientsConfig.name

urlpatterns = [
    path('', ClientsListView.as_view(), name='clients_list'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>/', delete_client, name='delete_client'),
]
