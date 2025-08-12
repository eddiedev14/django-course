from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="challenges_dashboard"),
    path("<int:month>/", views.monthly_challenge, name="monthly_challenges"), # Dynamic Path Segment
]
