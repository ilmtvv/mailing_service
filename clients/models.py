from django.db import models

from users.models import User


class Client(models.Model):
    email = models.EmailField(max_length=25)
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{ self.email } { self.name }'

    class Meta:
        unique_together = [['email', 'name', 'users']]
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
