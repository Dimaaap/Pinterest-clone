from django import forms
from django.contrib.auth.hashers import check_password
from django.contrib import messages

from ..forms import SetUserAvatarForm
from ..messages_store import *


class Helper:

    @staticmethod
    def get_form_initial_values(form: forms,
                                initial_dict: dict) -> forms:
        """
        Метод, який встановлює значення за замовчуванням
        у поля форми.
        Приймає власне форму і словник, де ключ - назва поля,
        у яке потрібно вставити значення, а значення - значення поля
        Повертає ту ж форму з уже встановленими значеннями
        за замовчуванням
        """
        second_form = form(initial=initial_dict)
        return second_form

    @staticmethod
    def change_cleaned_data_dict(request, cleaned_data: dict):
        """
        Метод, який перевіряє, чи існує у словнику,
        який йому передали ключ "id", якщо не існує,
        поіератє помилку інакше встановлює id у значення id
        авторизованого користувача, який зайшов на цю сторінку.
        Також намагається видалити поле username, якщо такого немає,
        повертає помилку
        """
        if 'id' not in cleaned_data:
            raise KeyError("The dict must contains an 'id' key")
        cleaned_data["id"] = request.user.id
        try:
            del cleaned_data["username"]
        except KeyError:
            return False

    @staticmethod
    def form_user_full_name(field_values: dict, username: str) -> str:
        """
        Метод, який формує повне ім'я користувача, яке складається
        з імені й прізвища, якщо користувач їх вказав, або
        username в іншому випадку.
        """
        if "first_name" in field_values and "last_name" in field_values:
            full_name = f"{field_values['first_name']} {field_values['last_name']}"
        else:
            full_name = username
        return full_name

    @staticmethod
    def check_is_field_input(user_info):
        """
        Метод, який перевіряє, які дані про себе заповнив користувач.
        Приймає user_info, який є результатом роботи метода get()
        і повертає сформований словник, де ключем є назва поля, а
        значенням - дані, які туди ввів користувач
        """
        field_value_dict = {}
        for field_name, field_value in user_info.__dict__.items():
            if not (field_name.startswith("_") or
                    callable(field_value)) and field_value:
                field_value_dict[field_name] = field_value
        return field_value_dict

    @staticmethod
    def format_errors_message(error_obj):
        errors_dict = dict(error_obj)
        return list(errors_dict.values())
