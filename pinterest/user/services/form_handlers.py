from django.contrib import messages

from ..models import UserAdditionalInfo
from ..services.db_services import DBService
from ..services.helpers import Helper
from ..forms import UpdateUserInformationForm
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
            helper.change_cleaned_data_dict(request, form.cleaned_data)
            db_service.create_or_update_data_in_model(UserAdditionalInfo, **form.cleaned_data)
            db_service.filter_data_in_model_with_update(data_storage.USER_MODEL, "pk", request.user.id,
                                                        "username", username)
            return messages.success(request, SuccessMessages.update_data_in_model.value)
        else:
            return messages.error(request, ErrorMessages.error_update_data_in_model.value)
