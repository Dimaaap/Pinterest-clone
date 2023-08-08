import json

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse

from .forms import SigninForm, LoginForm
from .models import User
from .services import *


def main_page_view(request):
    if request.method == "POST" and "hidden" in request.POST:
        form = SigninForm(request.POST)
        if form.is_valid():
            email, password, birthday_date = form.cleaned_data.values()
            new_user = User.objects.create_user(email=email, password=password, birthday=birthday_date)
            new_user.save()
            print("Form valid")
            return JsonResponse({"result": "success"})
        else:
            handle_message_error = handle_error_messages_service(form.errors)
            return JsonResponse({"result": "error", "message": handle_message_error})
    elif request.method == "POST":
        handle_login_form_service(request)
    form = SigninForm()
    second_form = LoginForm()
    return render(request, "main/main_page.html", context={"form": form, "second_form": second_form})


def wall_page_view(request):
    return render(request, "main/wall_page.html")


def handle_login_form_service(request):
    pass
