from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    name = models.CharField(max_length=155, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=155, unique=True, null=True)
    brand = models.CharField(max_length=155, default="", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutriscore = models.CharField(max_length=255, default="", null=True)
    url = models.CharField(max_length=255, default="", null=True)
    img_url = models.CharField(max_length=255, default="", null=True)
    fat = models.CharField(max_length=155, unique=True, null=True)
    kcal = models.CharField(max_length=155, unique=True, null=True)
    proteins = models.CharField(max_length=155, unique=True, null=True)

    def __str__(self):
        return self.name

class Substitute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    note = models.IntegerField(null=True, default=1,
        validators = [
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return self.product.name