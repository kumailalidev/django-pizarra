from django.urls import path
from . import views

# Django app namespace
app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
]
