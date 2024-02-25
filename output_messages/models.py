from django.db import models

from users.models import User


class OutputMessage(models.Model):

    title = models.CharField(max_length=25)
    body = models.TextField(null=True, blank=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        unique_together = [['title', 'users']]
        verbose_name = 'OutputMessage'
        verbose_name_plural = 'OutputMessages'