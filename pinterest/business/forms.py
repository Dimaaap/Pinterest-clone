from django import forms

from .models import *
from .data_storage import DataStorage

data_storage = DataStorage()


class BusinessDetailForm(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        fields = ("business_name", "is_site_exists", "business_site", "country_or_region", "language")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    business_name = forms.CharField(label="Ім'я профілю", widget=forms.TextInput(attrs={"class": "form-control"}))
    is_site_exists = forms.ChoiceField(label="У вас є веб-сайт?",
                                       widget=forms.RadioSelect,
                                       choices=data_storage.IS_SITE_EXISTS_CHOICE
                                       )
    business_site = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    country_or_region = forms.ChoiceField(label="Країна або регіон", choices=data_storage.COUNTRIES_LIST,
                                          required=False,
                                          initial="Ukraine",
                                          widget=forms.Select(attrs={
                                              "class": "select form-control",
                                              "id": "select-region"
                                          }
                                          ))
    language = forms.ChoiceField(label="Мова", required=False, choices=data_storage.LANGUAGES_LIST,
                                 initial="Ukrainian",
                                 widget=forms.Select(attrs={
                                     "class": "select form-control",
                                     "id": "select-language"
                                 }))


class BusinessDescriptionForm(forms.ModelForm):
    class Meta:
        model = BusinessDescription
        fields = ('business_niche', 'business_aim')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    business_niche = forms.ChoiceField(label="Укажіть сферу діяльності компанії",
                                       required=True, choices=data_storage.COMPANIES_NICHE,
                                       widget=forms.Select(attrs={
                                           "class": "select form-control",
                                           "id": "select-niche"
                                       }))
    business_aim = forms.MultipleChoiceField(label="Які цілі ви ставите", choices=data_storage.COMPANIES_AIM,
                                             widget=forms.CheckboxSelectMultiple())


class CompanyDescriptionForm(forms.ModelForm):
    class Meta:
        model = BusinessDescription
        fields = ("business_description",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    business_description = forms.ChoiceField(label="Опишіть свою компанію",
                                             required=True, choices=data_storage.COMPANIES_DESCRIPTION,
                                             widget=forms.RadioSelect)


class IsAddInterestingForm(forms.ModelForm):
    class Meta:
        model = BusinessProfile
        fields = ("would_like_start_add",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    would_like_start_add = forms.ChoiceField(label="Чи цікавить вас розміщення реклами на Pinterest",
                                             required=True, choices=data_storage.START_ADD_CHOICE,
                                             widget=forms.RadioSelect)
