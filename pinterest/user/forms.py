from django import forms
from django.contrib.auth import get_user_model

from .parse_data import get_list_all_countries
from policy.parse_languages import get_country_list

LANGUAGES_LIST = get_country_list()

USER_MODEL = get_user_model()
GENDER_CHOICE = [
    (1, "Чоловіча"),
    (2, "Жіноча"),
    (3, "Інша стать")
]

COUNTRIES_LIST = get_list_all_countries()


class SetUserAvatarForm(forms.ModelForm):
    class Meta:
        model = USER_MODEL
        fields = ("avatar",)

    avatar = forms.ImageField(label="Обрати фото", widget=forms.FileInput(attrs={"class": "change-confirm",
                                                                                 "title": " "}))


class UpdateUserInformationForm(forms.Form):
    first_name = forms.CharField(label="Ім'я",
                                 widget=forms.TextInput(attrs={"class": "form-control shorter",
                                                               "id": "first-name"}))
    last_name = forms.CharField(label="Прізвище",
                                widget=forms.TextInput(attrs={"class": "form-control shorter",
                                                              "id": "last-name"}))
    bio = forms.CharField(label="Про вас",
                          widget=forms.Textarea(attrs={"class": "form-textarea",
                                                       "placeholder": "Розкажіть свою історію",
                                                       "id": "desc",
                                                       'cols': 40, "rows": 4}))
    personal_site = forms.URLField(label="Сайт",
                                   widget=forms.URLInput(attrs={"class": "form-control",
                                                                "placeholder":
                                                                    "Додайте посилання, щоб збільшити трафік сайту",
                                                                "id": "site-link"}))
    username = forms.CharField(label="Ім'я користувача",
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control",
                                                             "id": "username"}))

    def clean_first_name(self):
        first_name = self.first_name
        if not first_name:
            raise forms.ValidationError("Профіль повинен мати ім'я")
        return first_name

    def clean_last_name(self):
        last_name = self.last_name
        if not last_name:
            raise forms.ValidationError("Профіль повинен мати ім'я")
        return last_name


class UserAccountDataForm(forms.Form):
    email = forms.EmailField(label="Електронна пошта - Приватно", widget=forms.EmailInput(attrs={
        "class": "form-control",
        "id": "email-field"
    }))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "id": "password-field"
    }))
    birth_day = forms.DateField(label="Дата народження", widget=forms.DateInput(attrs={
        "class": "form-control",
        "id": "date-field",
        "type": "date",
    }))
    gender = forms.ChoiceField(label="Стать", choices=GENDER_CHOICE, widget=forms.RadioSelect(attrs={
        "class": "radio-select",
        "id": "gender-select-field"
    }))
    country_or_region = forms.ChoiceField(label="Країна або регіон", choices=COUNTRIES_LIST,
                                          initial="Ukraine",
                                          widget=forms.Select(attrs={
                                              "class": "select form-control",
                                              "id": "select-region"
                                          }
                                          ))
    language = forms.ChoiceField(label="Мова", choices=LANGUAGES_LIST, widget=forms.Select(attrs={
        "class": "select form-control",
        "id": "select-language"
    }))
