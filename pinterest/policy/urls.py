from django.urls import path, include

from .views import *

urlpatterns = [
    path("", main_policy_view, name="main_policy"),
    path("/terms", terms_of_usage_view, name="usage_terms")
]