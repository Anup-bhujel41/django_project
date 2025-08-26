#where we define the urls which will redirect to the view functions
from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="index")
]