from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .forms import SetUserAvatarForm
from .validators import image_validator
from .service import *
from .models import UserAdditionalInfo

USER_MODEL = get_user_model()


@login_required
def profile_page_view(request, username):
    user = get_data_from_model(USER_MODEL, "username", f"@{username}")
    user_info = get_data_from_model(UserAdditionalInfo, "pk", request.user.id)
    field_values = check_is_field_input(user_info)
    if not user:
        return redirect("/user-wall")
    account_type = request.user.is_personal
    request.session["username"] = username
    context = {"username": username, "login": request.user.email,
               "account_type": account_type, "avatar": request.user.avatar}
    return render(request, "user/main_profile_page.html", context)


def check_is_field_input(user_info):
    field_value_dict = {}
    for field_name, field_value in user_info.__dict__.items():
        if not (field_name.startswith("_") or callable(field_value)) and field_value:
            field_value_dict[field_name] = field_value
    return field_value_dict




@login_required
def settings_profile_page_view(request):
    avatar = request.user.avatar
    if request.method == "POST" and "username" not in request.POST:
        form = SetUserAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            new_avatar = request.FILES['avatar']
            is_valid = image_validator(new_avatar)
            if isinstance(is_valid, str):
                return messages.error(request, is_valid)
            else:
                current_user = get_data_from_model(USER_MODEL, "email", request.user.email)
                current_user.avatar = new_avatar
                current_user.save()
            return JsonResponse({"new_image_url": current_user.avatar.url})
    elif request.method == "POST" and "username" in request.POST:
        upload_user_info_form_handler(request)
    form = SetUserAvatarForm()
    user_data = get_data_from_model(UserAdditionalInfo, "id", request.user.id)
    if user_data:
        second_form = get_form_initial_values(request, user_data)
    context = {"username": request.session.get("username"),
               "avatar": avatar, "form": form,
               "second_form": second_form}
    return render(request, "user/settings_profile.html", context)


@login_required
def add_account_page_view(request):
    return render(request, "user/add_account_page.html")
