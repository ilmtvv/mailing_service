from django import template

from config import settings

register = template.Library()

@register.simple_tag
def image_tag(url):
    return f'{settings.MEDIA_URL}{url}'