from django.db import models
from django.db import connections
from django.contrib.auth.models import User
from PIL import Image
 

class category(models.Model):
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    feature=models.BooleanField(default=False)
    image=models.ImageField(upload_to='pics',default='SOME STRING')
    

    def __str__(self):
        return self.title
    class Meta: 
        verbose_name = "Categorie"

class service(models.Model):
    title=models.CharField(max_length=200)
    image=models.ImageField(upload_to='pics',default='SOME STRING')
    description=models.TextField()
    feature=models.CharField(max_length=200)
    price=models.IntegerField(default=10)
    category=models.ForeignKey(category,  on_delete=models.CASCADE)
    featured=models.BooleanField(default=False)
    visible=models.BooleanField(default=True)
class comments(models.Model):
    comment=models.TextField()
    rating=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    service=models.ForeignKey(service,on_delete=models.CASCADE)
    created_at=models.DateTimeField( auto_now_add=True)
    class Meta: 
        verbose_name = "Review"
    
    
    