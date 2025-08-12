from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="challenges"),
    path("january/", views.january_challenges, name="january"),
    path("february/", views.february_challenges, name="february")
]
