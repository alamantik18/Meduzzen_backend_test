from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db import models

from .manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, verbose_name='username')
    email = models.EmailField(verbose_name='email address', unique=True)
    password = models.CharField(max_length=255, verbose_name='Password', default='')
    register_date = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email