from django.shortcuts import render, redirect

from .forms import SigninForm


def main_page_view(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = SigninForm()
    return render(request, "main/main_page.html", context={"form": form})
