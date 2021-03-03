from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError


def signup(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html", {'form':UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                newuser = User.objects.create_user(request.POST["username"], None, request.POST["password1"])
                User.save(newuser)
                login(request, newuser)
                return redirect("frontpage")
            except IntegrityError:
                return render(request, "accounts/signup.html", {'form':UserCreationForm(), 'error':'Ce pseudo est déjà utilisé.'})
        else:
            return render(request, "accounts/signup.html", {'form':UserCreationForm(), 'error':'Les mots de passe ne correspondent pas.'})

def loginuser(request):
    if request.method == "GET":
        return render(request, "accounts/signin.html", {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "accounts/signin.html", {'form':AuthenticationForm(), 'error':'Le pseudo et le mot de passe ne correspondent pas.'})
        else:
            login(request, user)
            return redirect("frontpage")

def return_to_frontpage(request):
    return render(request, "../frontpage/frontpage/index.html")

def signout(request):
    if request.method == 'POST':
        logout(request)
        return redirect("frontpage")

def displayprofile(request):
    return render(request, "accounts/profile.html")