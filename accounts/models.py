from django.db import models
from django.contrib.auth.models import AbstractUser


class UserMail(AbstractUser):
    email = models.EmailField()