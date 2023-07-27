import datetime

from django import forms

from .models import User


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
    birthday_field = forms.DateField(required=True, label="Дата народження",
                                     widget=forms.DateInput(attrs={"class": "form-control birthday",
                                                                   "id": "birthday_input",
                                                                   "type": "date"}))

    def clean_password(self):
        password = str(self.cleaned_data["password"])
        if len(password) < 6:
            raise forms.ValidationError("Надто легкий пароль.Він повинен містити 6 і більше символів")
        return password

    def clean_email(self):
        email = str(self.cleaned_data["email"])
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError("Користувач з таким email уже інсує на сайті")

    def clean_birthday_field(self):
        birthday = str(self.cleaned_data["birthday_field"])
        birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
        if birthday_date > datetime.date.today():
            raise forms.ValidationError("Здається ви ввели неправильне значення дати")
        return birthday


