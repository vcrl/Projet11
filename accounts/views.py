"""
Vues correspondant à l'application 'accounts' qui
gère toutes les requêtes liées à l'authentification
"""
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import SignUpForm, LoginForm


def signup(request):
    """
    Fonction servant à traiter les requêtes liées
    à l'inscription d'un utilisateur sur l'application.
    """
    if request.method == "GET":
        return render(request, "accounts/signup.html", {'form':SignUpForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                newuser = User.objects.create_user(request.POST["username"], request.POST['email'], request.POST["password1"])
                User.save(newuser)
                login(request, newuser)
                return redirect("frontpage")
            except IntegrityError:
                return render(request, "accounts/signup.html", {'form':SignUpForm(), 'error':'Ce pseudo est déjà utilisé.'})
        else:
            return render(request, "accounts/signup.html", {'form':SignUpForm(), 'error':'Les mots de passe ne correspondent pas.'})

def loginuser(request):
    """
    Fonction servant à traiter les requêtes liées
    à la connexion d'un utilisateur sur l'application.
    """
    if request.method == "GET":
        return render(request, "accounts/signin.html", {'form':LoginForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "accounts/signin.html", {'form':LoginForm(), 'error':'Le mail et le mot de passe ne correspondent pas.'})
        else:
            login(request, user)
            return redirect("frontpage")

def return_to_frontpage(request):
    """
    Fonction servant à traiter les requêtes liées
    à l'inscription d'un utilisateur sur l'application.
    """
    return render(request, "../frontpage/frontpage/index.html")

def signout(request):
    """
    Fonction servant à traiter les requêtes liées
    à la déconnexion d'un utilisateur sur l'application.
    """
    if request.method == 'POST':
        logout(request)
        return redirect("frontpage")

def displayprofile(request):
    """
    Fonction servant à traiter les requêtes liées
    à l'affichage du profil d'unutilisateur sur 
    l'application.
    """
    return render(request, "accounts/profile.html")