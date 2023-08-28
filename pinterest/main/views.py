from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect

from .forms import SigninForm, LoginForm
from .services import *
from .form_handler import MainFormsHandler


def main_page_view(request):
    if request.method == "POST" and "hidden" in request.POST:
        form = SigninForm(request.POST)
        if form.is_valid():
            MainFormsHandler.signin_form_handler(form)
            return JsonResponse({"result": "success"})
        else:
            handle_message_error = handle_error_messages_service(form.errors)
            return JsonResponse({"result": "error", "message": handle_message_error})
    elif request.method == "POST":
        handle_login_form(request)
    form = SigninForm()
    second_form = LoginForm()
    return render(request, "main/main_page.html", context={"form": form, "second_form": second_form})


def wall_page_view(request):
    return render(request, "main/wall_page.html")


def handle_login_form(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        user = MainFormsHandler.login_form_handler(request, login_form)
        if user:
            return redirect(wall_page_view)
        else:
            return messages.error(request, "Неправильний логін або пароль")
    else:
        messages.error(request, "Неправильний логін або пароль")
    return redirect(wall_page_view)
