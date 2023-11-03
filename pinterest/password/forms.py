from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password

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


class PasswordMatchValidator:
    def __init__(self, user):
        self.user = user

    def __call__(self, value):
        if not self.user or not self.user.check_password(value):
            raise forms.ValidationError("Ви ввели неправильне значення паролю")


class UpdatePasswordFormAccountSettings(forms.Form):
    old_password = forms.CharField(max_length=55, label="Старий пароль - Забули?",
                                   required=False,
                                   widget=forms.PasswordInput(attrs={
                                       "class": "form-input"
                                   }),
                                   validators=[PasswordMatchValidator(user=None)])

    new_password = forms.CharField(max_length=55, label="Новий пароль",
                                   required=False,
                                   widget=forms.PasswordInput(attrs={
                                       "class": "form-input"
                                   }))

    new_password_repeat = forms.CharField(max_length=55, label="Введіть пароль повторно",
                                          required=False,
                                          widget=forms.PasswordInput(attrs={
                                              "class": "form-input"
                                          }))

    def __init__(self, user, *args, **kwargs):
        super(UpdatePasswordFormAccountSettings, self).__init__(*args, **kwargs)
        self.fields['old_password'].validators[0] = PasswordMatchValidator(user=user)


    def clean_new_password(self):
        new_password = self.cleaned_data.get("new_password")
        if len(new_password) < 8:
            print("It`s too short password")
            raise forms.ValidationError("Пароль повинен містити не менше 8 символів")
        if all([i.isdigit() for i in new_password]) or all([i.isalpha() for i in new_password]):
            raise forms.ValidationError("Пароль містити хоча б одну цифру і літеру англійського алфівіту")
        return new_password

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        new_password_repeat = cleaned_data.get("new_password_repeat")
        if new_password != new_password_repeat:
            raise forms.ValidationError("Значення паролів не співпадають")
        return cleaned_data
