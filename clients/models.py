from django.db import models

from users.models import User


class Client(models.Model):
    email = models.EmailField(max_length=25, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    comment = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['email', 'first_name', 'last_name']]

