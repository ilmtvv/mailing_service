from django.db import models

from mailings.models import Mailing
from users.models import User


class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) # users
    mailing = models.ForeignKey(Mailing, on_delete=models.DO_NOTHING)   # mailing.title
    time = models.DateTimeField(auto_now_add=True)
    responce_mailing = models.CharField(max_length=25)  # ?
    responce_server = models.CharField(max_length=25)   # ?

    def __str__(self):
        return f'{ self.time }'

    class Meta:

        verbose_name = 'Log'
        verbose_name_plural = 'Logs'
