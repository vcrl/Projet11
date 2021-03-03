from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Product, Substitute

# Create your views here.
def display_substitutes(request):
    substitutes = Substitute.objects.all()
    return render(request, "research/substitutes.html", {'substitutes':substitutes})