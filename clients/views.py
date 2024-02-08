from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from clients.models import Client


class ClientsListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'first_name', 'last_name', 'comment',)
    success_url = reverse_lazy('clients:clients_list')
