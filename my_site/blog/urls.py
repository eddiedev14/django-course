from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="blog"),
    path("posts/", views.allPosts, name="posts")
]
