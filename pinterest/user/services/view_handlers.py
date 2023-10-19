from django.shortcuts import redirect
from django.contrib import messages

from ..data_storage import *
from ..services.db_services import *
from ..services.helpers import *
from ..models import UserAdditionalInfo
from ..forms import SetUserAvatarForm, \
    UpdateUserInformationForm, UserAccountDataForm
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

    def profile_page_view_get_context(self):
        account_type = self.request.user.is_personal
        self.request.session["username"] = self.username
        full_name = self.profile_page_view_handler()[0]
        context = {"username": self.username,
                   "login": self.request.user.email,
                   "account_type": account_type,
                   "avatar": self.request.user.avatar,
                   "full_name": full_name}
        return context

    def settings_profile_page_view(self):
        current_user = ""
        form = SetUserAvatarForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            new_avatar = self.request.FILES['avatar']
            is_valid = image_validator(new_avatar)
            if isinstance(is_valid, str):
                return messages.error(self.request, is_valid)
            else:
                current_user = self.db_service.get_data_from_model(data_storage.USER_MODEL,
                                                                   "email", self.request.user.email)
                current_user.avatar = new_avatar
                current_user.save()
        return current_user

    def settings_profile_page_view_initialization(self):
        user_data = self.db_service.get_data_from_model(UserAdditionalInfo, "id", self.request.user.id)
        if user_data:
            initial_values = {"username": self.request.user.username,
                              "first_name": user_data.first_name,
                              "last_name": user_data.last_name,
                              "bio": user_data.bio, "personal_site": user_data.personal_site}
            second_form = UpdateUserInformationForm(initial=initial_values)
            return second_form

    def settings_profile_page_view_get_context(self):
        avatar = self.request.user.avatar
        form = SetUserAvatarForm()
        second_form = self.settings_profile_page_view_initialization()
        context = {"username": self.request.session.get("username"),
                   "avatar": avatar, "form": form,
                   "second_form": second_form,
                   "full_name": self.request.session.get("full_name")}
        return context

    def account_settings_page_view(self):
        if self.request.method == "POST":
            form = UserAccountDataForm(self.request.POST)
            if form.is_valid():
                pass