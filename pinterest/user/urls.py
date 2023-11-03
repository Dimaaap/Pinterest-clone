from django.urls import path

from .views import *


urlpatterns = [
    path("me/<str:username>/", profile_page_view, name="profile_page"),
    path("add-account", add_account_page_view, name="add-account"),
    path("settings/edit-profile", settings_profile_page_view, name="settings-profile"),
    path("settings/account-settings", account_settings_page_view, name="account-settings"),
    path("convert-business", convert_business_page_view, name="convert_business")
]