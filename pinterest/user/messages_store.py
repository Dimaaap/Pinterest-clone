from enum import Enum


class SuccessMessages(Enum):
    update_data_in_model = "Ваші дані успішно збережено"


class ErrorMessages(Enum):
    error_update_data_in_model = "Упс...здається виникла якась помилка",
    input_wrong_password = "Неправильно введений пароль",
    password_are_unequal = "Значення паролів не співпадають",
    too_short_password = "Пароль повинен бути в дожину не менше 8 символів",
    password_syntax_error = "Пароль повинен містити хоча б одну цифру і англійську літеру"