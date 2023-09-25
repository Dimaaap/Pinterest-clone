import uuid
from time import time

import jwt

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.conf import settings

from .managers import CustomUserManager


class User(AbstractBaseUser):
    user_id = models.UUIDField(
        default=uuid.uuid4,
        editable=False
    )
    email = models.EmailField(max_length=155, unique=True)
    username = models.CharField(max_length=155, default="")
    password = models.CharField(max_length=255)
    birthday = models.DateField(auto_now_add=True, null=False)
    is_personal = models.BooleanField(default=True)
    is_commercial = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def set_username_automatically(self):
        self.username = f"@{str(self.email).split()[0]}"

    def check_personal_and_commercial_different(self):
        if self.is_commercial and self.is_personal:
            self.is_personal = False
        if self.is_commercial and not self.is_personal:
            self.is_personal = True

    def save(self, *args, **kwargs):
        self.set_username_automatically()
        self.check_personal_and_commercial_different()
        super(User, self).save(*args, **kwargs)

    def get_reset_password_token(self, expires_in=1440):
        return jwt.encode({
            "reset_password": self.pk, "exp": time() + expires_in
        }, settings.SECRET_KEY, algorithm="HS256")

    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])['reset_password']
        except Exception as e:
            print(e)
            return
        return User.objects.get(pk=id)
