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
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(label="Прізвище",
                                widget=forms.TextInput(attrs={"class": "form-control"}))
    profile_description = forms.CharField(label="Про вас",
                                          widget=forms.Textarea(attrs={"class": "form-textarea",
                                                                       "placeholder": "Розкажіть свою історію"}))
    site_link = forms.URLField(label="Сайт",
                               widget=forms.URLInput(attrs={"class": "form-control",
                                                            "placeholder":
                                                                "Додайте посилання, щоб збільшити трафік сайту"}))
    username = forms.CharField(label="Ім'я користувача",
                               widget=forms.TextInput(attrs={"class": "form-control"}))

