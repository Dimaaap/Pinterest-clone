from dataclasses import dataclass

from django.contrib.auth import get_user_model

from .parse_data import get_list_all_countries
from policy.parse_languages import get_country_list


@dataclass
class DataStorage:
    LANGUAGES_LIST = get_country_list()
    USER_MODEL = get_user_model()
    GENDER_CHOICE = [
        (1, "Чоловіча"),
        (2, "Жіноча"),
        (3, "Інша стать")
    ]
    COUNTRIES_LIST = get_list_all_countries()
    MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10 MB
    ALLOWED_FILE_FORMATS = {"JPEG", "JPG", "PNG", "GIF"}
