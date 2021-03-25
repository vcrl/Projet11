"""
Formulaires de l'application 'accounts'
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    """
    Formulaire d'inscription sur l'application
    """
    username = forms.EmailField(max_length=254) # Serves as email to login
    username.label = "Pseudo :"
    password1 = forms.CharField(widget=forms.PasswordInput)
    password1.label = "Mot de passe :"
    password2 = forms.CharField(widget=forms.PasswordInput)
    password2.label = "Retapez votre mot de passe :"
    email = forms.CharField(max_length=254)
    email.label = "Adresse mail :"

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    """
    Formulaire de connexion sur l'application
    """
    username = forms.CharField(max_length=254)
    username.label = "Pseudo/Email :"
    password = forms.CharField(widget=forms.PasswordInput)
    password.label = "Mot de passe :"

    class Meta:
        model = User
        fields = ('username', 'password1')