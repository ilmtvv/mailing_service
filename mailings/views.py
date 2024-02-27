import datetime
import sys

from crontab import CronTab
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from config.settings import BASE_DIR
from mailings.models import Mailing
from utils.create_cron_jobs import create_cron_jobs


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

        create_cron_jobs(self.object)

        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')
    fields = ('message', 'clients', )
    extra_context = {
        'title': 'Update',
    }


class DeleteMailingView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()

        cron = CronTab(user=True)   # обложить бы это место ловушками на ошибки
        comment = str(self.object.pk)
        cron.remove_all(comment=comment)
        cron.write()

        return HttpResponseRedirect(success_url)
