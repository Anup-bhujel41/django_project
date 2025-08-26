from django.urls import path
from biodata2 import views


urlpatterns = [
    path('biodata/', views.landing_page, name="biodata")
]