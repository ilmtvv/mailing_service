from django.views.generic import ListView

from logs.models import Log


class LogListView(ListView):
    model = Log

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
