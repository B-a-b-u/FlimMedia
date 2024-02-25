from django.urls import path
from .views import Home,Individual_post,Add_post


urlpatterns = [
    path("",Home.as_view(), name="home"), # Home page url
    path("post/<int:pk>",Individual_post.as_view(), name="individual_post"), # Individual post page url
    path("add_post/",Add_post.as_view(), name="add_post"), # Home page url


]