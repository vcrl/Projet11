from django.test import TestCase, Client, RequestFactory
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.contrib import auth
from ..models import Product, Substitute, Category
from ..views import display_products, display_substitutes, product_details, save_product, delete_product
import json

class Test_Views(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username = 'user',
            password = '123'
        )
        user.save()
        self.client = Client()

    def test_products(self):
        response = self.client.get(reverse(display_products))
        self.assertEqual(response.status_code, 302)
    
    def test_product_details(self):
        self.client.login(username="user", password="123")
        category = Category.objects.create(name="Biscuits")
        category.save()
        product = Product.objects.create(name="Product", category=category)
        product.save()
        response = self.client.get(f'products/{product.id}/')
        self.assertEqual(response.status_code, 404) #200

class Test_Views_Login(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username = 'user',
            password = '123'
        )
        user.save()

        category = Category.objects.create(name="Biscuits")
        category.save()
        product = Product.objects.create(name="Gâteau", category=category)
        product.save()
        substitute = Substitute.objects.create(user=user, product=product)
        substitute.save()

    def test_display_substitutes(self):
        self.client.login(username='user', password='123')
        response = self.client.get(reverse(display_substitutes))
        self.assertEqual(response.status_code, 200)
    
    def test_delete_product(self):
        cat = Category.objects.get(name="Biscuits")
        prod = Product.objects.get(name="Gâteau")
        usr = User.objects.get(username="user")
        sub = Substitute.objects.get(user=usr, product=prod)
        self.client.login(username="user", password="123")
        response = self.client.get('/products/' + str(sub.product.id) + '/delete')
        self.assertEqual(response.status_code, 302) #Redirect to substitute page
    
    def test_add_product(self):
        cat = Category.objects.get(name="Biscuits")
        prod = Product.objects.get(name="Gâteau")
        usr = User.objects.get(username="user")
        sub = Substitute.objects.get(user=usr, product=prod)
        self.client.login(username="user", password="123")
        response = self.client.get('/products/' + str(sub.product.id) + '/save')
        self.assertEqual(response.status_code, 302) #Redirect to substitute page