from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Product, Substitute

def manager_display_products(search, page_number):
    products = Product.objects.all().filter(name__icontains=search)
    products_paginator = Paginator(products, 6)
    page = products_paginator.get_page(page_number)
    return {"count":products_paginator.count, "page":page}