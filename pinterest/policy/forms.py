from django import forms

from .parse_languages import get_country_list

LANGUAGES_LIST = get_country_list()


class SelectLanguageForm(forms.Form):
    language = forms.CharField(label="Мови:",
                               widget=forms.Select(choices=LANGUAGES_LIST,
                                                   attrs={"class": "form-control"}))
    
