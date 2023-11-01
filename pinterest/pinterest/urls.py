from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('password', include("password.urls")),
    path("policy", include("policy.urls")),
    path("user/", include("user.urls")),
    path("frontend/", index, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
