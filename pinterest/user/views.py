from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse

from .forms import SetUserAvatarForm, UpdateUserInformationForm
from .validators import image_validator

USER_MODEL = get_user_model()


@login_required
def profile_page_view(request, username):
    try:
        user = USER_MODEL.objects.get(username=f"@{username}")
    except ObjectDoesNotExist:
        return redirect('/user-wall')
    account_type = request.user.is_personal
    request.session["username"] = username
    context = {"username": username, "login": request.user.email,
               "account_type": account_type, "avatar": request.user.avatar}
    return render(request, "user/main_profile_page.html", context)


@login_required
def settings_profile_page_view(request):
    avatar = request.user.avatar
    print(request.POST)
    if request.method == "POST":
        form = SetUserAvatarForm(request.POST, request.FILES)
        if form.is_valid():
            new_avatar = request.FILES['avatar']
            is_valid = image_validator(new_avatar)
            if isinstance(is_valid, str):
                return messages.error(request, is_valid)
            else:
                current_user = USER_MODEL.objects.get(email=request.user.email)
                current_user.avatar = new_avatar
                current_user.save()
                return JsonResponse({"new_image_url": current_user.avatar.url})
    form = SetUserAvatarForm()
    second_form = UpdateUserInformationForm()
    context = {"username": request.session.get("username"),
               "avatar": avatar, "form": form,
               "second_form": second_form}
    return render(request, "user/settings_profile.html", context)


@login_required
def add_account_page_view(request):
    return render(request, "user/add_account_page.html")
