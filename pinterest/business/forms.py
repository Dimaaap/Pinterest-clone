from django import forms

from .models import *

IS_SITE_EXISTS_CHOICE = (
    (1, "Так"),
    (2, "Ні")
)


class BusinessDetailForm(forms.ModelForm):

    class Meta:
        model = BusinessProfile
        fields = ("business_name", "avatar", "is_site_exists", "business_site", "country_or_region", "language")

    business_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    avatar = forms.ImageField(widget=forms.FileInput(attrs={"class": "upload-avatar-image"}))
    is_site_exists = forms.ChoiceField(widget=forms.RadioSelect(choices=IS_SITE_EXISTS_CHOICE,
                                                                attrs={"class": "select-field"}))
    business_site = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
