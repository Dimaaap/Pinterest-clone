from django.contrib.auth.hashers import check_password
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def check_if_new_password_service(user, new_password: str):
    current_password = user.password
    return check_password(new_password, current_password)


def send_email_service(user_email, token):
    html_message = render_to_string("password/email.html", {"email": user_email, "token": token})
    email = EmailMessage("Скидання паролю", html_message, settings.EMAIL_HOST_USER, [user_email])
    email.content_subtype = "html"
    email.fail_silently = False
    email.send()


def set_user_new_password_service(password: str, user):
    user.set_password(password)
    user.save()