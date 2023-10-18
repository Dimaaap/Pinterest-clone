from typing import Any

from django.core.exceptions import ObjectDoesNotExist

from ..filters import EqualFilter
from ..data_storage import DataStorage

data_storage = DataStorage()


class DBService:
    """
    Клас, який містить у собі всі функції для роботою з базою даних.
    Для кожного методу, на приклад get() є свій метод
    """
    def __init__(self):
        self.eq_filter = EqualFilter()

    def get_data_from_model(self, model: data_storage.USER_MODEL,
                            key: str, value: Any) -> data_storage.USER_MODEL | bool:
        """
        Метод, який реалізовує функціонал методу get() Django ORM.
        Приймає модель, із якої потрібно вибрати дані, ключ, за яким
        потрібно шукати певний об'єкт і значення цього ключа
        Якщо об'єкт знайдений, повертає його, якщо ні - повертає
        False
        """
        try:
            data = model.objects.get(**self.eq_filter(key, value))
        except ObjectDoesNotExist:
            return False
        return data

    def filter_data_in_model(self, model: data_storage.USER_MODEL, key: str,
                             value: Any) -> data_storage.USER_MODEL:
        """
        Метод, який реалізовує filter iз Django ORM.
        Приймає ті ж аргументи, що й get_data_from_model
        Повертає результат пошуку, тобто QuerySet
        """
        data = model.objects.filter(**self.eq_filter(key, value))
        return data

    def filter_data_in_model_with_update(self, model: data_storage.USER_MODEL,
                                         key: str, value: Any, set_key: str,
                                         set_value: Any) -> None:
        """
        Метод, який спочатку шукає потрібні дані, використовуючи
        метод filter_data_in_model(), а потім оновлює їх на основі
        отриманих від користувача даних
        Приймає model - Модель даних, на основі якої буде
        відбуватись фільтрація і оновлення даних
        key - ключове поле, за яким будуть фільтруватись дані
        value - значення цього поля
        set_key - поле, значення якого потрібно оновити
        set_value - значення, яке потрібно встановити для цього поля
        Нічого не повертає
        """
        filtered_data = self.filter_data_in_model(model, key, value)
        filtered_data.update(**self.eq_filter(set_key, set_value))

    @staticmethod
    def create_or_update_data_in_model(model: data_storage.USER_MODEL, **fields_values) -> None:
        """
        Метод, який реалізвує функціонал методу update_or_create
        Django ORM
        Для початку перевіряє, чи інсує у переданому йому словнику
        ключ id, якщо ні - повертає KeyError
        Інакше фільтрує дані моделі за цим ключем id і, якщо
        записів із таким id в моделі немає - створює, якщо є -
        оновлює
        """
        if "id" not in fields_values:
            raise KeyError("The dict must contain 'id' key")
        model.objects.update_or_create(
            id=fields_values["id"],
            defaults=fields_values
        )
