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
    def check_is_user_passwords_equal(request, input_password: str, user_password: str):
        """
        Статичний метод, який перевіряє, чи значення паролю, яке ввів користувач збігається зі значенням паролю,
        яке розміщене в базі даних
        Приймає input_password - значення паролю, яке увів користувач
        user_password - пароль користувача в БД
        """
        if check_password(input_password, user_password):
            return True
        return "Неправильно введений пароль"

    @staticmethod
    def check_are_new_passwords_equal(request, new_password: str, repeat_new_password: str):
        """
        Метод, який приймає введене значення нового паролю користувача і повторне значення паролю користувача
        і перевіряє, чи вони рівні, якщо рівні - повертає True, інакше - повідомлення про помилку
        new_password - Значення поля "Новий пароль" у формі зміни паролю
        repeat_new_password - Значення поля "Повторіть пароль" у формі зміни паролю
        """
        if new_password == repeat_new_password:
            return True
        return "Значення паролів не співпадають"

    @staticmethod
    def check_is_password_valid(request, password: str):
        """
        Метод, який перевіряє валідність паролю, тобто, чи його довжина більше 8-ми символів і
        чи пароль не містить лише цифри або лише літери. Валідний пароль повинен бути від 8-ми
        символів у довжину і містити як цифри, так і літери англійського алфавіту.
        Приймає об'єкт request - об'єкт сесії користувача
        password - Значення паролю, введеного користувачем
        У випадку, якщо пароль валідний повертає True - інакше об'єкт messages.error із
        повідомленням про помилку
        """
        if len(password) < 8:
            return "Пароль повинен бути в дожину не менше 8 символів"
        if all([i.isdigit() for i in password]) or all([i.isalpha() for i in password]):
            return "Пароль повинен містити хоча б одну цифру і англійську літеру"
        return True

    def is_valid_form(self, request, input_password: str, user_password: str, new_password: str,
                      repeat_new_password: str):
        """
        Загальний метод валідації, який виконує методи валідації check_is_user_passwords_equal,
        check_are_new_passwords_equal і check_is_password_valid.
        Якщо всі методи повернули True, тоді і цей метод повертає True, а інакше повертає об'єкт
        messages.error методу, який повернув
        """
        validation_methods_set = {self.check_is_user_passwords_equal(request, input_password, user_password),
                                  self.check_are_new_passwords_equal(request, new_password, repeat_new_password),
                                  self.check_is_password_valid(request, new_password)
                                  }
        valid_form = True
        messages_list = []
        for i in validation_methods_set:
            if not isinstance(i, bool):
                messages_list.append(i)
        if not messages_list:
            return valid_form
        return messages_list
