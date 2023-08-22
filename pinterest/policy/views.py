from django.shortcuts import render

from .models import HeaderChapter


def main_policy_view(request):
    all_chapters_list = HeaderChapter.objects.all()
    return render(request, "policy/main_page.html", context={"chapters": all_chapters_list})