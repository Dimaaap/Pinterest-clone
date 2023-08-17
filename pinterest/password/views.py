from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth import get_user_model
from django.http import JsonResponse

from .forms import FindUserForm, SetNewPasswordForm

USER_MODEL = get_user_model()


def reset_password_view(request):
    if request.method == "POST":
        form = FindUserForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["email"]
            try:
                current_user = USER_MODEL.objects.get(email=user_email)
                token = current_user.get_reset_password_token()
                request.session["token"], request.session["email"] = token, user_email
                html_message = render_to_string("password/email.html", {"email": user_email, "token": token})
                email = EmailMessage("Скидання паролю", html_message, settings.EMAIL_HOST_USER, [user_email])
                email.content_subtype = "html"
                email.fail_silently = False
                email.send()
                return JsonResponse({"status": "success"})
            except Exception as e:
                print(e)
                messages.error(request, "Виникла помилка при надсиланні листа на вашу адресу")
                return JsonResponse({"status": "false"})
        else:
            messages.error(request, "Помилка надсилання форми")
    else:
        form = FindUserForm()
    return render(request, "password/reset_password.html", {"form": form})


def create_new_password_view(request, user_email: str, user_token: str):
    current_user = USER_MODEL.objects.get(email=user_email)
    user = current_user.verify_reset_password_token(user_token)
    print(current_user, user)
    if not user:
        print(user)
        return redirect(reset_password_view)
    if request.method == "POST":
        form = SetNewPasswordForm(request.POST)
        if form.is_valid():
            pass
        else:
            return messages.error(request, "Упс...Схоже,щось пішло не так")
    else:
        form = SetNewPasswordForm()
    return render(request, "password/set_new_password.html", {"form": form})

