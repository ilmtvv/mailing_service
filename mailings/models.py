from datetime import datetime

from django.db import models
from django.utils import timezone

from clients.models import Client
from output_messages.models import OutputMessage
from users.models import User


class Mailing(models.Model):
    PERIODICITY_CHOICES = (
        ('D', 'Day'),
        ('W', 'Week'),
        ('M', 'Month'),
    )

    message = models.ForeignKey(OutputMessage, on_delete=models.CASCADE, null=True, blank=True)
    clients = models.ManyToManyField(Client)
    mailing_time = models.TimeField(default=timezone.now)
    periodicity = models.CharField(max_length=15, choices=PERIODICITY_CHOICES)
    mailing_status = models.IntegerField(default=0)

    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)



    def __str__(self):
        return f'{ self.message }'

    class Meta:

        verbose_name = 'Mailing'
        verbose_name_plural = 'Mailings'
