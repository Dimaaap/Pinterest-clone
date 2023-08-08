import uuid

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractBaseUser):
    user_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField(max_length=155, unique=True)
    password = models.CharField(max_length=255)
    birthday = models.DateField(auto_now_add=True, null=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email
