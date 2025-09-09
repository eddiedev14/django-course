from datetime import date
from django.http import Http404
from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def home(request):
    posts_content = []

    latests_posts = Post.objects.all()[:3]
    for post in latests_posts:
        post_tags = Tag.objects.filter(post_tags__post=post) #Obtener tags de un post
        posts_content.append({ "post": post, "tags": post_tags })

    return render(request, "blog/home.html", { "posts": posts_content})

def allPosts(request):
    posts_content = []

    latests_posts = Post.objects.all()
    for post in latests_posts:
        post_tags = Tag.objects.filter(post_tags__post=post) #Obtener tags de un post
        posts_content.append({ "post": post, "tags": post_tags })

    return render(request, "blog/posts.html", { "posts": posts_content })

def singlePost(request, id, path):
    selectedPost = get_object_or_404(Post, id=id)
    return render(request, "blog/singlePost.html", { "post": selectedPost })
