from django.urls import path
from .views import api_home

urlpatterns = [
    path("hello/", api_home)
]
