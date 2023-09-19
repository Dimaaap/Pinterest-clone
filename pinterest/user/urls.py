from django.urls import path

from .views import *


urlpatterns = [
    path("me/<str:username>/", profile_page_view, name="profile_page")
]