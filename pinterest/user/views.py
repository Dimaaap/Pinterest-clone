from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .services.form_handlers import FormHandler
from .services.view_handlers import *
from password.forms import UpdatePasswordFormAccountSettings

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
    context = ViewHandler(username, request).profile_page_view_get_context()
    context.update(field_values)
    return render(request, "user/main_profile_page.html", context)


@login_required
def settings_profile_page_view(request):
    if request.method == "POST" and "username" not in request.POST:
        current_user = ViewHandler(request.user.username, request).settings_profile_page_view()
        return JsonResponse({"new_image_url": current_user.avatar.url})
    elif request.method == "POST" and "username" in request.POST:
        form_handler.upload_user_info_form_handler(request)
    context = ViewHandler(request.user.username, request).settings_profile_page_view_get_context()
    return render(request, "user/settings_profile.html", context)


@login_required
def account_settings_page_view(request):
    if request.method == "POST" and "email" in request.POST:
        form = UserAccountDataForm(request.POST)
        if form.is_valid():
            form_handler.user_account_data_form_handler(request, form)
    elif request.method == "POST" and "email" not in request.POST:
        ViewHandler(request.user.username, request).account_settings_page_view()
        modal_form = UpdatePasswordFormAccountSettings(user=request.user, data=request.POST)
        if modal_form.is_valid():
            return JsonResponse({"success": "Пароль успішно змінено"})
        else:
            errors = helper.format_errors_message(modal_form.errors)
            return JsonResponse({"errors": errors})
    else:
        form = ViewHandler(request.user.username, request).account_settings_page_view()
    modal_form = UpdatePasswordFormAccountSettings(user=request.user)
    context = {"username": request.user.username, "form": form, "modal_form": modal_form}
    return render(request, "user/account_settings_page.html", context)


@login_required
def add_account_page_view(request):
    return render(request, "user/add_account_page.html")


@login_required
def convert_business_page_view(request):
    context = {"username": request.user.username}
    return render(request, "user/convert_business_page.html", context=context)