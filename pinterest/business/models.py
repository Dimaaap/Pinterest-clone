import uuid

from django.db import models
from django.contrib.auth import get_user_model

from multiselectfield import MultiSelectField


USER_MODEL = get_user_model()

BUSINESS_AIM_CHOICES = [
    ("More sell", "Продати більше товарів"),
    ("Lead Generation", "Створити більше лідів для компанії"),
    ("Increase traffic", "Збільшити трафік на сайт"),
    ("Increase audience", "Створити вміст на Pinterest, щоб збільшити аудиторію"),
    ("Improve famous", "Підвищити впізнаваність бренду"),
    ("Don`t know", "Ще не знаю")
]

COMPANY_DESCRIPTION_CHOICE = [
    (1, "Не можу сказати напевно"),
    (2, "Блогер"),
    (3, "Товари, продукти або послуги споживчого призначення"),
    (4, "Підрядник або постачальник послуг"),
    (5, "Автор, лідер думок, громадський діяч або знаменитість"),
    (6, "Місцевий роздрібний магазин або компанія"),
    (7, "Онлайн-магазин або майданчик доя онлайн-торгівлі"),
    (8, "Видавець або представник ЗМІ"),
    (9, "Інше")
]

START_ADD_CHOICE = [
    (1, "Так, мене цікавить реклама"),
    (2, "Ні, мене не цікавить реклама"),
    (3, "Ще не знаю")
]


class BusinessProfile(models.Model):
    user_id = models.ForeignKey(USER_MODEL, on_delete=models.SET_NULL, null=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    business_name = models.CharField(max_length=100, default="")
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    is_site_exists = models.BooleanField(default=True)
    business_site = models.URLField(max_length=100, null=True, default=None)
    country_or_region = models.CharField(max_length=50, null=True, default=None)
    language = models.CharField(max_length=100, null=True, default=None)
    would_like_start_add = models.IntegerField(choices=START_ADD_CHOICE)

    def __str__(self):
        return f'{self.user}  {self.id}'

    def validate_business_site(self):
        site_exists = self.is_site_exists
        if not site_exists:
            self.business_site = None

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.validate_business_site()


class BusinessDescription(models.Model):
    business_id = models.ForeignKey(BusinessProfile, on_delete=models.SET_NULL, null=True)
    business_niche = models.CharField(max_length=35, null=True, default="")
    business_aim = MultiSelectField(choices=BUSINESS_AIM_CHOICES, max_choices=3, max_length=100)
    business_description = models.IntegerField(choices=COMPANY_DESCRIPTION_CHOICE)

    def __str__(self):
        return f'{self.business_id} {self.business_niche}'
