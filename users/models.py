import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.EmailField(unique=True, null=True)
    #email = models.CharField(max_length=25, unique=True)
    is_active = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
