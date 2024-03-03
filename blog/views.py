from django.shortcuts import render
from django.views.generic import DetailView

from blog.models import BlogUnit


class BlogUnitDetailView(DetailView):
    model = BlogUnit

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()

        return self.object
