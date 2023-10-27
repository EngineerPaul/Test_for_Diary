from django.urls import path

from .views import CaseWhenPage

urlpatterns = [
    path("", CaseWhenPage.as_view(), name="case_when_url"),
]
