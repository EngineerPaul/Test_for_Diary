from django.urls import path

from .views import GetUserInfoPage

urlpatterns = [
    path("", GetUserInfoPage.as_view(), name="get_user_info_url"),
]
