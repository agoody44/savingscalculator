from django.urls import path
from savings_calculator import views
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("calculate/", views.calculate, name="calculate"),
]

urlpatterns += staticfiles_urlpatterns()