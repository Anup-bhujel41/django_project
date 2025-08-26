from django.urls import path
from . import views

urlpatterns = [
    path("home", views.landing_page, name="landing"),
    path("test", views.form, name="test"),
    path("test2", views.form2, name="test2")
]