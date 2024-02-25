from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    title = models.CharField(max_length=100)
    blog = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("individual_post",args=str(self.id))