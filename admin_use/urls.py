from django.urls import path

from . import views

urlpatterns = [
    path("show", views.show),
    path("refresh", views.refresh),
    path("logout", views.refresh),

]