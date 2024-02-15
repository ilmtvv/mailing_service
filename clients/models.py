from django.db import models
from django.http import request

from users.models import User


class Client(models.Model):
    email = models.EmailField(max_length=25, unique=True)
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True,)

    class Meta:
        unique_together = [['email', 'name', 'users']]
        verbose_name = 'client'
        verbose_name_plural = 'clients'
