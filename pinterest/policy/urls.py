from django.urls import path, include

from .views import *

urlpatterns = [
    path("", main_policy_view, name="main_policy"),
    path("terms", terms_of_usage_view, name="usage_terms"),
    path("confidence", confidence_policy_view, name="confidence_policy"),
    path("community_guidelines", community_guidelines_view, name="community_guidelines"),
    path("merchant_guidelines", merchant_guidelines_view, name="merchant_guidelines"),
    path("advertising_guidelines", advertising_guidelines_view, name="advertising_guidelines"),
    path("developers_guidelines", developers_guidelines_view, name="developers_guidelines"),
    path("copyright", copyright_view, name="copyright"),
    path("trademark", trademark_view, name="trademark"),
    path("enforcement", enforcement_view, name="enforcement"),
    path("transparency", transparency_view, name="transparency"),
    path("transparency_report", transparency_report_view, name="transparency_report"),
    path("notice-at-collection", notice_at_collection_view, name="notice_at_collection"),
]