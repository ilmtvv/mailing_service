from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from logs.models import Log


class LogListView(LoginRequiredMixin, ListView):
    model = Log

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        if self.request.user.is_superuser:
            queryset = super().get_queryset()
        return queryset
