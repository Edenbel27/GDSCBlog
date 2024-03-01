from django.db import models
from django.utils import timezone
from BlogApp.models import Post

class Comment(models.Model):

    Content = models.TextField()
    Author = models.CharField(max_length=250)
    Publish= models.DateTimeField(default = timezone.now)
    Post= models.ForeignKey(Post, on_delete=models.CASCADE)
    

def __str__(self):
    return self.Content
