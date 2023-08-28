from django.contrib.auth import authenticate, login

from .models import User


class MainFormsHandler:

    @staticmethod
    def signin_form_handler(form):
        email, password, birthday_date = form.cleaned_data.values()
        new_user = User.objects.create_user(email=email, password=password, birthday=birthday_date)
        new_user.save()

    @staticmethod
    def login_form_handler(request, form):
        email, password = form.cleaned_data.values()
        user = authenticate(request, email=email, password=password)
        if user is None:
            return False
        login(request, user)
        return True