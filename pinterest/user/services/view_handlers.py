from django.shortcuts import redirect
from django.contrib import messages

from ..data_storage import *
from ..services.db_services import *
from ..services.helpers import *
from ..models import UserAdditionalInfo
from ..forms import SetUserAvatarForm
from ..validators import image_validator


class ViewHandler:

    def __init__(self, username, request):
        self.username = username
        self.db_service = DBService()
        self.data_storage = DataStorage()
        self.request = request
        self.helper = Helper()

    def profile_page_view_handler(self):
        user = self.db_service.get_data_from_model(self.data_storage.USER_MODEL, "username",
                                                   f"@{self.username}")
        user_info = self.db_service.get_data_from_model(UserAdditionalInfo, "pk",
                                                        self.request.user.id)
        field_values = self.helper.check_is_field_input(user_info)
        full_name = self.helper.form_user_full_name(field_values, self.username)
        self.request.session["full_name"] = full_name
        if not user:
            return False, False
        return full_name, field_values

    def settings_profile_page_view(self):
        avatar = self.request.user.avatar
        if self.request.method == "POST" and "username" in self.request.POST:
            form = SetUserAvatarForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                new_avatar = self.request.FILES["avatar"]
                is_valid = image_validator(new_avatar)
                if isinstance(is_valid, str):
                    return messages.error(self.request, is_valid)
                else:
                    current_user = self.db_service.get_data_from_model(self.data_storage.USER_MODEL,
                                                                       "email", self.request.user.email)
                    current_user.avatar = new_avatar
                    current_user.save()

