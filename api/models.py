from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=700)
    price = models.FloatField()
    location = models.CharField(max_length=300)
    imgUrl = models.URLField()
    isSold = models.BooleanField(default=False)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='models')
    
    def __str__(self):
        return self.name


class Buyer(models.Model):
    name = models.CharField(max_length=150)
    phoneNumber = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank= True, related_name = 'models')
    
    def __str__(self):
        return self.name
