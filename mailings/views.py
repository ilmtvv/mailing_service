from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mailings.models import Mailing


class MailingListView(ListView):
    model = Mailing

    def get_queryset(self):
        return super().get_queryset().filter(users=self.request.user)


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('message', 'clients', 'mailing_time', 'periodicity',)
    success_url = reverse_lazy('mailings:mailing_list')
    extra_context = {
        'title': 'Add',
    }

    def form_valid(self, form):
        self.object = form.save()
        self.object.users = self.request.user
        self.object.save()
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')
    fields = ('message', 'clients', 'mailing_time', 'periodicity',)
    extra_context = {
        'title': 'Update',
    }


class DeleteMailingView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')
