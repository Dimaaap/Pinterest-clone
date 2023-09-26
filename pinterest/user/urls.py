from django.urls import path

from .views import *


urlpatterns = [
    path("me/<str:username>/", profile_page_view, name="profile_page"),
    path("add-account", add_account_page_view, name="add-account"),
    path("settings/edit-profile", settings_profile_page_view, name="settings-profile")
]