from dataclasses import dataclass

from django.contrib.auth import get_user_model


@dataclass
class DataStorage:
    USER_MODEL = get_user_model()