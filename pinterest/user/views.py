from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required

from .forms import SetUserAvatarForm

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
    if request.method == "POST":
        print(request.POST)
        form = SetUserAvatarForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SetUserAvatarForm()
    context = {"username": request.session.get("username"),
               "avatar": avatar, "form": form}
    return render(request, "user/settings_profile.html", context)


@login_required
def add_account_page_view(request):
    return render(request, "user/add_account_page.html")
