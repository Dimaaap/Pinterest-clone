from typing import Any

from django.core.exceptions import ObjectDoesNotExist

from ..filters import EqualFilter
from ..data_storage import DataStorage

data_storage = DataStorage()


class DBService:
    def __init__(self):
        self.eq_filter = EqualFilter()

    @staticmethod
    def get_data_from_model(model: data_storage.USER_MODEL, key: str, value: Any) -> data_storage.USER_MODEL | bool:
        eq_filter = EqualFilter()
        try:
            data = model.objects.get(**eq_filter(key, value))
        except ObjectDoesNotExist:
            return False
        return data

    @staticmethod
    def filter_data_in_model(model: data_storage.USER_MODEL, key: str, value: Any) -> data_storage.USER_MODEL:
        eq_filter = EqualFilter()
        data = model.objects.filter(**eq_filter(key, value))
        return data

    def filter_data_in_model_with_update(self, model: data_storage.USER_MODEL, key: str, value: Any, set_key: str,
                                         set_value: Any) -> None:
        eq_filter = EqualFilter()
        filtered_data = self.filter_data_in_model(model, key, value)
        filtered_data.update(**eq_filter(set_key, set_value))

    @staticmethod
    def create_or_update_data_in_model(model: data_storage.USER_MODEL, **fields_values) -> None:
        if "id" not in fields_values:
            raise KeyError("The dict must contain 'id' key")
        model.objects.update_or_create(
            id=fields_values["id"],
            defaults=fields_values
        )
