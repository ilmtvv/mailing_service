from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from output_messages.models import OutputMessage


class MessagesListView(ListView):
    model = OutputMessage

    def get_queryset(self):
        return super().get_queryset().filter(users=self.request.user)


class MessageCreateView(CreateView):
    model = OutputMessage
    fields = ('title', 'body',)
    success_url = reverse_lazy('messages:messages_list')
    extra_context = {
        'title': 'Add',
    }

    def form_valid(self, form):
        self.object = form.save()
        self.object.users = self.request.user
        self.object.save()
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = OutputMessage
    success_url = reverse_lazy('messages:messages_list')
    fields = ('title', 'body',)
    extra_context = {
        'title': 'Update',
    }


class DeleteMessageView(DeleteView):
    model = OutputMessage
    success_url = reverse_lazy('messages:messages_list')