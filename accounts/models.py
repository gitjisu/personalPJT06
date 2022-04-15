
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    sex = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.pk}'