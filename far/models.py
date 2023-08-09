from django.db import models

# Create your models here.
class farmer(models.Model):
    name= models.CharField(max_length=25)
    address=models.CharField(max_length=25)
    email=models.EmailField(max_length=100)
    product=models.CharField(max_length=25)
    type=models.CharField(max_length=100)
    
    
    
    doc= models.TextField()
    

