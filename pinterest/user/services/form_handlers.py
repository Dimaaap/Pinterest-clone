from django.contrib import messages

from ..models import UserAdditionalInfo, UserPersonalData
from ..services.db_services import DBService
from ..services.helpers import Helper
from ..forms import UpdateUserInformationForm, UserAccountDataForm
from ..data_storage import DataStorage
from ..messages_store import *

helper = Helper()
db_service = DBService()
data_storage = DataStorage


class FormHandler:

    @staticmethod
    def upload_user_info_form_handler(request):
        form = UpdateUserInformationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            form.cleaned_data["id"] = request.user.id
            helper.change_cleaned_data_dict(request, form.cleaned_data)
            db_service.create_or_update_data_in_model(UserAdditionalInfo, **form.cleaned_data)
            db_service.filter_data_in_model_with_update(data_storage.USER_MODEL, "pk", request.user.id,
                                                        "username", username)
            return messages.success(request, SuccessMessages.update_data_in_model.value)
        else:
            return messages.error(request, ErrorMessages.error_update_data_in_model.value)

    @staticmethod
    def user_account_data_form_handler(request, form):
        user = db_service.get_data_from_model(data_storage.USER_MODEL, "id", request.user.id)
        birth_day = form.cleaned_data["birth_day"]
        country_or_region = form.cleaned_data["country_or_region"]
        language = form.cleaned_data["language"]
        gender = form.cleaned_data["gender"]
        password = form.cleaned_data["password"]
        request["password"] = password
        field_values = {"id": user.id, "birth_date": birth_day,
                        "country_or_region": country_or_region,
                        "language": language,
                        "gender": gender}
        db_service.create_or_update_data_in_model(UserPersonalData, **field_values)

    @staticmethod
    def change_password_modal_form_handler(request, form):
        user = db_service.get_data_from_model(data_storage.USER_MODEL, "id", request.user.id)
        old_password, new_password, new_password_repeat = (form.cleaned_data["old_password"],
                                                           form.cleaned_data["new_password"],
                                                           form.cleaned_data["new_password_repeat"])
        user_model_password = user.password
        if helper.is_valid_form(request, old_password, user_model_password, new_password, new_password_repeat):
            user.set_password(new_password)
            user.save()

