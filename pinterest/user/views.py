from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .services.form_handlers import FormHandler
from .services.view_handlers import *
from password.forms import UpdatePasswordFromAccountSettings

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
    print(request.POST)
    if request.method == "POST" and "email" in request.POST:
        form = UserAccountDataForm(request.POST)
        if form.is_valid():
            form_handler.user_account_data_form_handler(request, form)
    elif request.method == "POST" and "email" not in request.POST:
        print("In this fork")
        form = ViewHandler(request.user.username, request).account_settings_page_view()
        modal_form = UpdatePasswordFromAccountSettings(request.POST)
        if modal_form.is_valid():
            result = form_handler.change_password_modal_form_handler(request, modal_form)
            if isinstance(result, bool):
                return JsonResponse({"success": "Пароль успішно змінено"})
            else:
                return JsonResponse({"errors": result})
        else:
            errors = format_errors_message(modal_form.errors)
            print(errors)
            return JsonResponse({"errors": errors})
        # return handler_change_password_form(request)
    else:
        form = ViewHandler(request.user.username, request).account_settings_page_view()
    modal_form = UpdatePasswordFromAccountSettings()
    context = {"username": request.user.username, "form": form, "modal_form": modal_form}
    return render(request, "user/account_settings_page.html", context)


def format_errors_message(error_obj):
    errors_dict = dict(error_obj)
    print(errors_dict)
    print(list(errors_dict.values())[0])
    return list(errors_dict.values())[0]


def handler_change_password_form(request):
    print("In handler method")
    modal_form = UpdatePasswordFromAccountSettings(request.POST)
    if modal_form.is_valid():
        result = form_handler.change_password_modal_form_handler(request, modal_form)
        if isinstance(result, bool):
            print("first response")
            return JsonResponse({"success": "Пароль успішно змінено"})
        else:
            print("second response")
            return JsonResponse({"errors": result})
    else:
        print("third response")
        return JsonResponse({"error": modal_form.errors})


@login_required
def add_account_page_view(request):
    return render(request, "user/add_account_page.html")
