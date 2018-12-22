from django.urls import path
from mbta import views

urlpatterns = [
    path("", views.home, name="home"),
    path("route/<route_id>/", views.detail, name="detail"),
]

