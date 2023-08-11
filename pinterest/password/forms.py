from django import forms
from django.core.exceptions import ObjectDoesNotExist

from main.models import User


class FindUserForm(forms.Form):
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(
                                 attrs={
                                        "placeholder": "Пошук",
                                        "class": "find-input"
                                        }))

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.onjects.get(email=email)
        except ObjectDoesNotExist:
            raise forms.ValidationError("Користувача із таким email не чув би")
        return email

