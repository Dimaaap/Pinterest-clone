from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .filters import EqualFilter
from .forms import UpdateUserInformationForm
from .models import UserAdditionalInfo
from .messages_store import *
from .data_storage import DataStorage

data_storage = DataStorage()


def get_data_from_model(model, key, value):
    eq_filter = EqualFilter()
    try:
        data = model.objects.get(**eq_filter(key, value))
    except ObjectDoesNotExist:
        return False
    return data


def filter_data_in_model(model, key, value):
    eq_filter = EqualFilter()
    data = model.objects.filter(**eq_filter(key, value))
    return data


def filter_data_in_model_with_update(model, filtered_key, filtered_value,
                                     set_key, set_value):
    eq_filter = EqualFilter()
    filtered_data = filter_data_in_model(model, filtered_key, filtered_value)
    filtered_data.update(**eq_filter(set_key, set_value))


def create_or_update_data_in_model(model, **fields_values):
    obj, created = model.objects.update_or_create(
        id=fields_values["id"],
        defaults=fields_values
    )


def get_form_initial_values(request, user_data):
    initial_dict = {"username": request.user.username, "first_name": user_data.first_name,
                    "last_name": user_data.last_name, "bio": user_data.bio,
                    "personal_site": user_data.personal_site}
    second_form = UpdateUserInformationForm(initial=initial_dict)
    return second_form


def change_cleaned_data_dict(request, cleaned_data: dict):
    cleaned_data["id"] = request.user.id
    try:
        del cleaned_data["username"]
    except KeyError:
        pass


def upload_user_info_form_handler(request):
    form = UpdateUserInformationForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        change_cleaned_data_dict(request, form.cleaned_data)
        create_or_update_data_in_model(UserAdditionalInfo, **form.cleaned_data)
        filter_data_in_model_with_update(data_storage.USER_MODEL, "pk", request.user.id, "username", username)
        return messages.success(request, SuccessMessages.update_data_in_model.value)
    else:
        return messages.error(request, ErrorMessages.error_update_data_in_model.value)


def form_user_full_name(field_values: dict, username: str):
    if "first_name" in field_values and "last_name" in field_values:
        full_name = f'{field_values["first_name"]} {field_values["last_name"]}'
    else:
        full_name = username
    return full_name


def check_is_field_input(user_info):
    field_value_dict = {}
    for field_name, field_value in user_info.__dict__.items():
        if not (field_name.startswith("_") or callable(field_value)) and field_value:
            field_value_dict[field_name] = field_value
    return field_value_dict
