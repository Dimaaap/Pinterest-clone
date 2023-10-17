from django.urls import path

from .views import *

urlpatterns = [
    path("reset", reset_password_view, name="reset-password"),
    path("pw/<str:user_email>/<str:user_token>/", create_new_password_view, name="create-new-password")
]