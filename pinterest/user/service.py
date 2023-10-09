from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from django.contrib import messages

from .filters import EqualFilter
from .forms import UpdateUserInformationForm
from .models import UserAdditionalInfo
from .messages_store import *

USER_MODEL = get_user_model()


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
        filter_data_in_model_with_update(USER_MODEL, "pk", request.user.id, "username", username)
        return messages.success(request, SuccessMessages.update_data_in_model.value)
    else:
        return messages.error(request, ErrorMessages.error_update_data_in_model.value)