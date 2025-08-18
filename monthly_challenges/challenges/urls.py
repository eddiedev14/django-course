from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="challenges_dashboard"),
    path("<int:month>/", views.monthly_challenge_by_number, name="monthly_challenges_by_number"), # Dynamic Path Segment
    path("<str:month>/", views.monthly_challenge, name="monthly_challenges"), # Dynamic Path Segment
]
