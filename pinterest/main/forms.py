from django import forms


class SigninForm(forms.Form):
    email = forms.EmailField(max_length=150, required=True, label="Адреса електронної пошти",
                             widget=forms.EmailInput(attrs={"class": "form-control",
                                                            "id": "email_input",
                                                            "placeholder": "Уведіть адресу ел. пошти",
                                                            "autocomplete": "off"}))
    password = forms.CharField(max_length=150, required=True, label="Пароль",
                               widget=forms.PasswordInput(attrs={"class": "form-control password",
                                                                 "id": "password_input",
                                                                 "placeholder": "Створіть пароль",
                                                                 "autocomplete": "off"}))
    birthday_field = forms.DateField(required=False, label="Дата народження",
                                     widget=forms.DateInput(attrs={"class": "form-control birthday",
                                                                   "id": "birthday_input"}))
