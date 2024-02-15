from django.contrib.sites import requests
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from clients.models import Client


class ClientsListView(ListView):
    model = Client

    def get_queryset(self):
        return super().get_queryset().filter(users=self.request.user)


class ClientCreateView(CreateView):
    model = Client
    fields = ('email', 'name', 'comment',)
    success_url = reverse_lazy('clients:clients_list')
    extra_context = {
        'title': 'Add',
    }

    def form_valid(self, form):
        self.object = form.save()
        self.object.users = self.request.user
        self.object.save()
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    model = Client
    success_url = reverse_lazy('clients:clients_list')
    fields = ('email', 'name', 'comment',)
    extra_context = {
        'title': 'Update',
    }


class DeleteClientView(DeleteView):
    model = Client
    success_url = reverse_lazy('clients:clients_list')


def delete_client(request, pk):
    Client.delete(Client.objects.get(pk=pk))
    return redirect(reverse_lazy('clients:clients_list'))
