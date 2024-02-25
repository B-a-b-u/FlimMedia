from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import Post


# home page view
class Home(ListView):
    model = Post
    template_name = "film_media_app\home.html"
    context_object_name = "posts"

# View for individual posts
class Individual_post(DetailView):
    model = Post
    template_name = "film_media_app\individual_post.html"
    context_object_name = "post"


# View for adding post
class Add_post(CreateView):
    model = Post
    template_name = "film_media_app\\add_post.html"
    context_object_name = "post"
    fields = "__all__"
    