from django.shortcuts import render
from django.conf import settings

from .models import HeaderChapter
from .forms import SelectLanguageForm

INITIAL_LANGUAGE = settings.INITIAL_LANGUAGE


def main_policy_view(request):
    all_chapters_list = HeaderChapter.objects.all()
    if request.method == "POST":
        form = SelectLanguageForm(request.POST)
        if form.is_valid():
            pass
        else:
            print("OOOps..form in invalid")
    else:
        form = SelectLanguageForm(initial={"language": INITIAL_LANGUAGE})
    return render(request, "policy/main_page.html", context={"chapters": all_chapters_list, "form": form})


def terms_of_usage_view(request):
    return render(request, "policy/usage_terms.html")


def confidence_policy_view(request):
    return render(request, "policy/confidence_policy.html")


def community_guidelines_view(request):
    return render(request, "policy/community_guidelines.html")


def merchant_guidelines_view(request):
    return render(request, "policy/merchant_guidelines.html")


def advertising_guidelines_view(request):
    return render(request, "policy/advertising_guidelines.html")


def developers_guidelines_view(request):
    return render(request, "policy/developers_guidelines.html")


def copyright_view(request):
    return render(request, "policy/copyright.html")


def trademark_view(request):
    return render(request, "policy/trademark.html")


def enforcement_view(request):
    return render(request, "policy/enforcement.html")


def transparency_view(request):
    return render(request, "policy/transparency.html")


def transparency_report_view(request):
    return render(request, "policy/transparency_report.html")


def notice_at_collection_view(request):
    return render(request, "policy/notice_at_collection.html")