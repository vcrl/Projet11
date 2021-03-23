from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=254)
    username.label = "Pseudo :"
    password1 = forms.CharField(widget=forms.PasswordInput)
    password1.label = "Mot de passe :"
    password2 = forms.CharField(widget=forms.PasswordInput)
    password2.label = "Retapez votre mot de passe :"
    email = forms.EmailField(max_length=254)
    email.label = "Adresse mail :"

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254)
    username.label = "Pseudo/Email :"
    email = forms.EmailField(max_length=254, unique=True)
    email.label = "Adresse mail :"
    password = forms.CharField(widget=forms.PasswordInput)
    password.label = "Mot de passe :"

    class Meta:
        model = User
        fields = ('username', 'password1')