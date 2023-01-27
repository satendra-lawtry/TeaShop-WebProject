from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)
    
    def __str__(self) -> str:
        return self.email
    
class Product(models.Model):
    pname = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to='media')
    description = models.TextField(max_length=500)
    
    def __str__(self) -> str:
        return self.pname