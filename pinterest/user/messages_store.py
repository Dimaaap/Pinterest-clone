from enum import Enum


class SuccessMessages(Enum):
    update_data_in_model = "Ваші дані успішно збережено"


class ErrorMessages(Enum):
    error_update_data_in_model = "Упс...здається виникла якась помилка"