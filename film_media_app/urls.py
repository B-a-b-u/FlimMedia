from django.urls import path
from .views import Home,Individual_post,Add_post, Update_post, Delete_post


urlpatterns = [
    path("",Home.as_view(), name="home"), # Home page url
    path("post/<int:pk>",Individual_post.as_view(), name="individual_post"), # Individual post page url
    path("add_post/",Add_post.as_view(), name="add_post"), # add post page url
    path("update_post/<int:pk>",Update_post.as_view(), name="update_post"), # update post page url
    path("delete_post/<int:pk>",Delete_post.as_view(), name="delete_post"), # delete post page url

]