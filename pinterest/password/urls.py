from django.urls import path

from .views import *

urlpatterns = [
    path("/reset", reset_password_view, name="reset-password")
]