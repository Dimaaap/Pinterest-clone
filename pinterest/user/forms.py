from django import forms
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class SetUserAvatarForm(forms.ModelForm):
    class Meta:
        model = USER_MODEL
        fields = ("avatar",)

    avatar = forms.ImageField(label="Обрати фото", widget=forms.FileInput(attrs={"class": "change-confirm",
                                                                                 "title": " "}))


class UpdateUserInformationForm(forms.Form):
    first_name = forms.CharField(label="Ім'я",
                                 required=False,
                                 widget=forms.TextInput(attrs={"class": "form-control shorter"}))
    last_name = forms.CharField(label="Прізвище",
                                required=False,
                                widget=forms.TextInput(attrs={"class": "form-control shorter",
                                                              "id": "last-name"}))
    profile_description = forms.CharField(label="Про вас",
                                          required=False,
                                          widget=forms.Textarea(attrs={"class": "form-textarea",
                                                                       "placeholder": "Розкажіть свою історію",
                                                                       'cols': 40, "rows": 4}))
    site_link = forms.URLField(label="Сайт",
                               required=False,
                               widget=forms.URLInput(attrs={"class": "form-control",
                                                            "placeholder":
                                                                "Додайте посилання, щоб збільшити трафік сайту"}))
    username = forms.CharField(label="Ім'я користувача",
                               required=False,
                               widget=forms.TextInput(attrs={"class": "form-control"}))

