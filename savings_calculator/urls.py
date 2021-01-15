from django.urls import path
from savings_calculator import views

urlpatterns = [
    path("", views.home, name="home"),
]