from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Product, Substitute
from .manager import manager_display_products

def display_substitutes(request):
    substitutes = Substitute.objects.filter(user=request.user)
    products_paginator = Paginator(substitutes, 6)
    page_number = request.GET.get("page")
    page = products_paginator.get_page(page_number)
    return render(request, "research/substitutes.html", {'count':products_paginator.count, "page":page})

def display_products(request):
    if request.method == "GET":
        try:
            search = request.GET.get("search")
            page_number = request.GET.get("page")
            data = manager_display_products(search, page_number)
            return render(request, "research/products.html", data)
        except ValueError:
            return redirect("frontpage")

def product_details(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    return render(request, "research/product.html", {"product":product})

def save_product(request, product_pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_pk)
        user = request.user
        substitute = Substitute(product=product, user=user)
        substitute.save()
        #return redirect("substitutes")
        return render(request, "research/product.html", {"product":product})
    else:
        return redirect("frontpage")

def delete_product(request, substitute_pk):
    if request.method == "POST":
        substitute = get_object_or_404(Substitute, pk=substitute_pk)
        user = request.user
        substitute.delete()
        return redirect("substitutes")
    else:
        return redirect("frontpage")