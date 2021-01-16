from django.urls import path
from savings_calculator import views
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create/",views.create, name='create'),
]