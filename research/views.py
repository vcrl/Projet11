"""
Vues de l'application "Research", permettant de traiter toutes
les requêtes liées à la recherche de produits
"""
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Product, Substitute, Rating
from .manager import manager_display_products
from .forms import RatingForm

@login_required
def display_substitutes(request):
    """
    Fonction permettant d'afficher les substituts
    enregistrés d'un utilisateur.
    La balise @login_required permet de n'afficher
    cette page que si l'utilisateur est connecté.
    """
    substitutes = Substitute.objects.filter(user=request.user)
    products_paginator = Paginator(substitutes, 6)
    page_number = request.GET.get("page")
    page = products_paginator.get_page(page_number)
    if User.is_authenticated:
        return render(request, "research/substitutes.html", {'count':products_paginator.count, "page":page})
    else:
        return redirect("frontpage")

def display_products(request):
    """
    Fonction permettant d'afficher les substituts
    enregistrés d'un utilisateur.
    La balise @login_required permet de n'afficher
    cette page que si l'utilisateur est connecté.
    """
    if request.method == "GET":
        try:
            search = request.GET.get("search")
            page_number = request.GET.get("page")
            data = manager_display_products(search, page_number)
            return render(request, "research/products.html", data)
        except ValueError:
            return redirect("frontpage")

def product_details(request, product_pk):
    """
    Fonction permettant d'afficher les détails
    d'un produit sur une page dédiée.
    """
    try:
        user = request.user
    except TypeError:
        pass

    product = get_object_or_404(Product, pk=product_pk)
    values = Rating.objects.filter(product=product).values('note')
    users = Rating.objects.filter(product=product).values('user_id')

    try:
        exists = Rating.objects.get(product=product, user=user)
        hasVoted = True
    except Rating.DoesNotExist:
        hasVoted = False
    except TypeError:
        hasVoted = False


    form = RatingForm()
    if values:
        final_note = 0
        count = 0
        for value in values:
            final_note += value["note"]
            count += 1
        _rating = final_note / count

        return render(request, "research/product.html", {"product":product, "rating":_rating, "hasVoted":hasVoted, "form":form})
    else:
        return render(request, "research/product.html", {"product":product, "hasVoted":hasVoted, "form":form})

@login_required
def save_product(request, product_pk):
    """
    Fonction permettant d'enregistrer un produit
    en substitut pour un utilisateur.
    La balise @login_required permet de n'afficher
    cette page que si l'utilisateur est connecté.
    """
    if request.method == "POST":
        product = get_object_or_404(Product, pk=product_pk)
        user = request.user
        substitute = Substitute(product=product, user=user)
        substitute.save()
        return redirect("substitutes")
    else:
        return redirect("frontpage")

@login_required
def delete_product(request, substitute_pk):
    """
    Fonction permettant de supprimer un substituts
    des enregistrés d'un utilisateur.
    La balise @login_required permet de n'afficher
    cette page que si l'utilisateur est connecté.
    """
    if request.method == "POST":
        substitute = get_object_or_404(Substitute, pk=substitute_pk)
        user = request.user
        substitute.delete()
        return redirect("substitutes")
    else:
        return redirect("frontpage")

def rate_product(request, product_pk):
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data.get('rating')

        product = get_object_or_404(Product, pk=product_pk)
        user = request.user
        rating = Rating.objects.create(product=product, user=user, note=note)

        values = Rating.objects.filter(product=product).values('note')
        users = Rating.objects.filter(product=product).values('user_id')
        try:
            exists = Rating.objects.get(product=product, user=user)
            hasVoted = True
        except Rating.DoesNotExist:
            hasVoted = False

        if values:
            final_note = 0
            count = 0
            for value in values:
                final_note += value["note"]
                count += 1
            _rating = final_note / count
        return render(request, "research/product.html", {"product":product, "rating":_rating, "hasVoted":hasVoted, "form":form})
