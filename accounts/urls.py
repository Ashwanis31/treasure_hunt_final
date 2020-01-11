from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login),
    path("register", views.register),
    path("puzzle", views.puzzle),
    path("logout", views.logout), 
    path("refresh", views.refresh),
    path("magiccard", views.magic_card),
    path("serial_start", views.serial_start), 
]