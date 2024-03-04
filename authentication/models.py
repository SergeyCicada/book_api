from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    ADMIN = "admin"
    MODERATOR = "moderator"
    UNKNOWN = "unknown"

    ROLE = [(ADMIN, ADMIN), (MODERATOR, MODERATOR), (UNKNOWN, UNKNOWN)]

    role = models.CharField(max_length=9, choices=ROLE, default=UNKNOWN)

