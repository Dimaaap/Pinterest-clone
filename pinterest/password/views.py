from django.shortcuts import render


def reset_password_view(request):
    return render(request, "password/reset_password.html")