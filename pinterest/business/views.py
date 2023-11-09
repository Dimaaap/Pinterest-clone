from django.shortcuts import render
from django.http import HttpResponse

from formtools.wizard.views import SessionWizardView

from .forms import *


def main_business_page_view(request):
    return render(request, "business/hub_page.html")


class FormsWizardView(SessionWizardView):
    form_list = [BusinessDetailForm, BusinessDescriptionForm, CompanyDescriptionForm, IsAddInterestingForm]
    template_name = 'business/hub_page.html'

    def done(self, form_list, **kwargs):
        return HttpResponse('Form submitted')

