from django.db import models
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class UserAdditionalInfo(models.Model):
    user_id = models.ForeignKey(USER_MODEL, on_delete=models.SET_NULL, null=True),
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    bio = models.TextField(blank=True, null=True)
    personal_site = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.user_id} - {self.first_name} {self.last_name}'

