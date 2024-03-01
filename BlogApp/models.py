from django.db import models

# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=30, unique= True)
    Content = models.TextField()
    Category = models.CharField(max_length=250)
    Image = models.ImageField(upload_to ='image/', blank= True)
    Tags = models.CharField(max_length=100,blank =True, null= True)

    
    
    def __str__ (self):
        return self.Title





 
