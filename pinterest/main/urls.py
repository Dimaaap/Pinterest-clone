from django.urls import path

from .views import *


urlpatterns = [
    path('', main_page_view, name='main_page'),
    path('user-wall/', user_wall_page_view, name="user_wall"),
    path('logout', logout_view, name="logout"),
]