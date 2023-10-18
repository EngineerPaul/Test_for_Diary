from django.urls import path

from .views import SassPage

urlpatterns = [
    path("", SassPage.as_view(), name="sass_url"),
]
