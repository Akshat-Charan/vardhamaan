from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

# models.py

class Product(models.Model):
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='products/')
    image2 = models.ImageField(upload_to='products/')
    image3 = models.ImageField(upload_to='products/')
    image4 = models.ImageField(upload_to='products/')
    image5 = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name
