from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from .forms import SetUserAvatarForm, UserAccountDataForm
from .validators import image_validator
from .models import UserAdditionalInfo, UserPersonalData
from .data_storage import DataStorage
from .services.db_services import DBService
from .services.helpers import Helper
from .services.form_handlers import FormHandler
from .services.view_handlers import *

data_storage = DataStorage()
db_service = DBService()
helper = Helper()
form_handler = FormHandler()


@login_required
def profile_page_view(request, username):
    full_name, field_values = ViewHandler(username,
                                          request).profile_page_view_handler()
    if not (full_name or field_values):
        return redirect('/user-wall')
    account_type = request.user.is_personal
    request.session["username"] = username
    context = {"username": username, "login": request.user.email,
               "account_type": account_type, "avatar": request.user.avatar,
               "full_name": full_name}
    context.update(field_values)
    return render(request, "user/main_profile_page.html", context)


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
                current_user = db_service.get_data_from_model(data_storage.USER_MODEL, "email", request.user.email)
                current_user.avatar = new_avatar
                current_user.save()
        return JsonResponse({"new_image_url": current_user.avatar.url})
    elif request.method == "POST" and "username" in request.POST:
        form_handler.upload_user_info_form_handler(request)
    form = SetUserAvatarForm()
    user_data = db_service.get_data_from_model(UserAdditionalInfo, "id", request.user.id)
    if user_data:
        initial_dict = {"username": request.user.username, "first_name": user_data.first_name,
                        "last_name": user_data.last_name, "bio": user_data.bio,
                        "personal_site": user_data.personal_site}
        second_form = helper.get_form_initial_values(form, initial_dict)
    context = {"username": request.session.get("username"),
               "avatar": avatar, "form": form,
               "second_form": second_form,
               "full_name": request.session.get("full_name")}
    return render(request, "user/settings_profile.html", context)


@login_required
def account_settings_page_view(request):
    if request.method == "POST":
        form = UserAccountDataForm(request.POST)
        if form.is_valid():
            user = data_storage.USER_MODEL.objects.get(id=request.user.id)
            birth_day = form.cleaned_data["birth_day"]
            country_or_region = form.cleaned_data["country_or_region"]
            language = form.cleaned_data["language"]
            gender = form.cleaned_data["gender"]
            print(gender)
            UserPersonalData.objects.update_or_create(id=user.id, defaults={
                "birth_date": birth_day,
                "country_or_region": country_or_region,
                "gender": gender,
                "language": language
            })
    else:
        form = UserAccountDataForm()
    user_data = db_service.get_data_from_model(data_storage.USER_MODEL, "id", request.user.id)
    try:
        user = UserPersonalData.objects.get(id=request.user.id)
        default_country_or_region = user.country_or_region if user.country_or_region != "Aruba" else "Aruba"
        default_language = user.language if user.language != "arabic" else "arabic"
        default_gender = user.gender if user.gender else None
        default_birthday = user.birth_date if user.birth_date else None
        print(default_birthday)
    except ObjectDoesNotExist:
        default_country_or_region = "Aruba"
        default_language = "arabic"
        default_gender = None
        default_birthday = None
    print(default_birthday)
    form = UserAccountDataForm(initial={"email": user_data, "country_or_region": default_country_or_region,
                                        "language": default_language,
                                        "gender": default_gender,
                                        "birth_day": default_birthday})
    context = {"username": request.user.username, "form": form}
    return render(request, "user/account_settings_page.html", context)


@login_required
def add_account_page_view(request):
    return render(request, "user/add_account_page.html")
