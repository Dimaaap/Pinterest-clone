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


def merhcant_guidelines_view(request):
    return render(request, "policy/merchant_guidelines.html")