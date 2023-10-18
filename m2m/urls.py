from django.urls import path

from .views import ManyToManyPage

urlpatterns = [
    path("", ManyToManyPage.as_view(), name="m2m_url"),
]
