from .forms import SelectLanguageForm


def change_language_form(request):
    form = SelectLanguageForm(request.POST)
    return {"language_form": form}
