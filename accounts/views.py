from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == "GET":
        return render(request, "accounts/signup.html", {'form':UserCreationForm()})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            newuser = User.objects.create_user(request.POST["username"], None, request.POST["password1"])
            User.save(newuser)
        else:
            print("not matching")
