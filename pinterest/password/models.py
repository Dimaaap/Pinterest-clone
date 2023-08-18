from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class UserPassword(models.Model):
    user = models.ManyToManyField(USER_MODEL)

