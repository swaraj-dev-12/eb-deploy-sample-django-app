
from django.contrib import admin
from django.urls import path
from user.views import health, home

urlpatterns = [
    path("", home),
    path("health", health)
]
