from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import SigninForm
from .models import User


def main_page_view(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            email, password, birthday_date = form.cleaned_data.values()
            new_user = User.objects.create_user(email=email, password=password, birthday=birthday_date)
            new_user.save()
            return redirect(wall_page_view)
        else:
            messages.error(request, "dadsadaada")
    else:
        form = SigninForm()
    return render(request, "main/main_page.html", context={"form": form})


def wall_page_view(request):
    return render(request, "main/wall_page.html")