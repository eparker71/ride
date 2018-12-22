from django.urls import path
from mbta import views

urlpatterns = [
    path("", views.home, name="home"),
]

