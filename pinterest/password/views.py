from django.shortcuts import render
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string

from .forms import FindUserForm


def reset_password_view(request):
    if request.method == "POST":
        form = FindUserForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data["email"]
            try:
                send_mail(subject="Скидання паролю", message="Скидання паролю",
                          from_email=settings.EMAIL_HOST_USER, recipient_list=[user_email])
            except Exception as e:
                print(e)
                messages.error(request, "Виникла помилка при надсиланні листа на вашу адресу")
        else:
            messages.error(request, "Помилка надсилання форми")
    else:
        form = FindUserForm()
    return render(request, "password/reset_password.html", {"form": form})