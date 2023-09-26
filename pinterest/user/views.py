from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

USER_MODEL = get_user_model()


def profile_page_view(request, username):
    if not request.user.is_authenticated:
        return redirect("/")
    try:
        user = USER_MODEL.objects.get(username=f"@{username}")
    except ObjectDoesNotExist:
        return redirect('/user-wall')
    account_type = request.user.is_personal
    request.session["username"] = username
    context = {"username": username, "login": request.user.email,
               "account_type": account_type, "avatar": request.user.avatar}
    return render(request, "user/main_profile_page.html", context)


def settings_profile_page_view(request):
    context = {"username": request.session.get("username")}
    return render(request, "user/settings_profile.html", context)


def add_account_page_view(request):
    return render(request, "user/add_account_page.html")
