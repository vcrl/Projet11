from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=155, unique=True)
    brand = models.CharField(max_length=155, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutriscore = models.CharField(max_length=255, default="")
    url = models.CharField(max_length=255, default="")
    img_url = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name

class Substitute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name