from django.shortcuts import render

from .forms import FindUserForm


def reset_password_view(request):
    if request.method == "POST":
        form = FindUserForm(request.POST)
    else:
        form = FindUserForm()
    return render(request, "password/reset_password.html", {"form": form})