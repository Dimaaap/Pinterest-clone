from django.shortcuts import render


def profile_page_view(request, username):
    return render(request, "user/main_profile_page.html")
