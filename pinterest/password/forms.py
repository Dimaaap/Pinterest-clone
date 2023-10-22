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
            User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise forms.ValidationError("Користувача із таким email не чув би")
        return email


class SetNewPasswordForm(forms.Form):
    new_password = forms.CharField(required=True,
                                   min_length=6,
                                   label="Новий пароль",
                                   widget=forms.PasswordInput(
                                       attrs={
                                           "class": "form-input"
                                       }
                                   ))
    repeat_new_password = forms.CharField(required=True,
                                          min_length=6,
                                          label="Повторіть новий пароль",
                                          widget=forms.PasswordInput(
                                              attrs={
                                                  "class": "form-input",
                                              }
                                          ))

    def clean_new_password(self):
        new_password = self.cleaned_data["new_password"]
        if all([i.isalpha() for i in new_password]) or all([i.isdigit() for i in new_password]):
            raise forms.ValidationError("Надто простий пароль.Він має містити хоча б одну цифру(1-9) і один символ")
        return new_password

    def clean_repeat_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        repeat_new_password = self.cleaned_data.get("repeat_new_password")
        if new_password and repeat_new_password and new_password != repeat_new_password:
            raise forms.ValidationError('Паролі не співпадають')
        return repeat_new_password


class UpdatePasswordFromAccountSettings(SetNewPasswordForm):
    old_password = forms.CharField(max_length=55, label="Старий пароль - Забули?",
                                   widget=forms.PasswordInput(attrs={
                                       "class": "form-input"
                                   }))
