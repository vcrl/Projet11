from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib import auth
from ..models import Product, Substitute, Category

class Test_Models(TestCase):
    def test_category_save_in_db(self):
        category = Category.objects.create(name="Biscuits")
        self.assertIs(category.name, "Biscuits")

    def test_product_save_in_db(self):
        category = Category.objects.create(name="Biscuits")
        product = Product.objects.create(name="Gâteau", category=category)
        self.assertIs(product.category, category)
        self.assertIs(product.name, "Gâteau")

    def test_substitute_save_in_db(self):
        user = User.objects.create(username="user", password="123")
        category = Category.objects.create(name="Biscuits")
        product = Product.objects.create(name="Gâteau", category=category)
        substitute = Substitute.objects.create(product=product, user=user)
        self.assertIs(substitute.product.name, "Gâteau")
        self.assertIs(substitute.user.username, "user")