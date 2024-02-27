from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from logs.models import Log


class LogListView(LoginRequiredMixin, ListView):
    model = Log

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
