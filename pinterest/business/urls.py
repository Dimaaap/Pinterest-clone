from django.urls import path

from .views import *


urlpatterns = [
    path('hub', main_business_page_view, name="hub")
]