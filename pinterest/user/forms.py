from django import forms
from django.contrib.auth import get_user_model

USER_MODEL = get_user_model()


class SetUserAvatarForm(forms.ModelForm):
    class Meta:
        model = USER_MODEL
        fields = ("avatar",)

    avatar = forms.ImageField(label="Обрати фото", widget=forms.FileInput(attrs={"class": "change-confirm",
                                                                                 "title": " "}))
