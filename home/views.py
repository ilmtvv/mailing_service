from django.core.cache import cache
from django.shortcuts import render

from blog.models import BlogUnit
from clients.models import Client
from config.settings import CACHE_ENABLED
from mailings.models import Mailing


def home_view(request): # как будто бы дофига запросов в базу данных,
    # но онож кешироваться будет, вот если бы как то разом за один заход вытянуть все
    # как то это можно было сделать ??
    if CACHE_ENABLED:
        key = 'blog_units_list'
        blog_units_list = cache.get(key)
        if blog_units_list is None:
            blog_units_list = BlogUnit.objects.all().order_by('?')[:3]
            cache.set(key, blog_units_list)
    else:
        blog_units_list = BlogUnit.objects.all().order_by('?')[:3]

    if request.user.is_authenticated:

        queryset = Mailing.objects.all().filter(users=request.user)
        mailings_all = queryset.count()

        mailing_activate = queryset.filter(mailing_status=1).count()
        queryset = Client.objects.all().filter(users=request.user)
        count_unique_clients = queryset.count()

        context = {
            'mailings_all': mailings_all,
            'mailing_activate': mailing_activate,
            'count_unique_clients': count_unique_clients,
            'blog_units_list': blog_units_list,

        }
    else:
        context = {
            'blog_units_list': blog_units_list,
        }
    print(blog_units_list)
    return render(request, 'home/home_list.html', context)
