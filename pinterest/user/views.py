from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

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
    if request.method == "POST":
        form = UserAccountDataForm(request.POST)
        if form.is_valid():
            form_handler.user_account_data_form_handler(request, form)
    else:
        form = UserAccountDataForm()
    form = ViewHandler(request.user.username, request).account_settings_page_view()
    context = {"username": request.user.username, "form": form}
    return render(request, "user/account_settings_page.html", context)


@login_required
def add_account_page_view(request):
    return render(request, "user/add_account_page.html")
