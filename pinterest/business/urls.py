from django.urls import path

from .views import *


urlpatterns = [
    path('hub', FormsWizardView.as_view(), name="hub")
]