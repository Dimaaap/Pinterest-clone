from django import forms


class SelectLanguageForm(forms.Form):
    language = forms.CharField(label="Мова:",
                               widget=forms.Select(choices=[],
                                                   attrs={"class": "form-control"}))
    
