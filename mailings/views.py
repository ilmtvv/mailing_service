import datetime
import sys

from crontab import CronTab
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from config.settings import BASE_DIR
from mailings.models import Mailing
from mailings.permissions import NotPermissionRequiredMixin
from utils.create_cron_jobs import create_cron_jobs


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing

    def get_queryset(self):
        if self.request.user.has_perm('mailings.manager'):
            return super().get_queryset()
        else:
            return super().get_queryset().filter(users=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
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


class MailingUpdateView(LoginRequiredMixin, NotPermissionRequiredMixin, UpdateView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')
    fields = ('message', 'clients', )
    extra_context = {
        'title': 'Update',
    }
    permission_required = 'mailings.manager'



class DeleteMailingView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        if self.request.user.has_perm('mailings.manager'):  # сделать проверку на принадлежность рассылки менеджеру
            return HttpResponseRedirect(success_url)
        else:
            self.object.delete()

            cron = CronTab(user=True)   # обложить бы это место ловушками на ошибки
            comment = str(self.object.pk)
            cron.remove_all(comment=comment)
            cron.write()

            return HttpResponseRedirect(success_url)


@login_required
@permission_required('mailings.manager')
def stop_mailing(request, pk):
    mailing = Mailing.objects.get(pk=pk)
    cron = CronTab(user=True)

    if mailing.mailing_status != 2:

        mailing.mailing_status = 2
        mailing.save()


        cron.remove_all(comment=str(mailing.pk))
        cron.write()
    elif mailing.mailing_status == 2:

        mailing.mailing_status = 0
        mailing.save()

        create_cron_jobs(mailing)

    return redirect(reverse_lazy('mailings:mailing_list'))
