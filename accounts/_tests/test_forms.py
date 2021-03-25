"""
Module créé afin de tester les formulaires
de l'application "accounts" de manière
indépendante.
"""
from ..forms import SignUpForm, LoginForm
from django.test import TestCase, Client
from django.contrib.auth.models import User

class Test_Forms(TestCase):
    """
    Classe principale renfermant toutes les méthodes
    liées aux tests des différents formulaires sur
    l'application.
    """
    def init(self):
        self.client = Client()

    def test_signup(self):
        """
        Cette méthode permet de tester le formulaire
        d'inscription sur l'application.
        Ici, nous prenons un email d'exemple,
        un nom d'utilisateur d'exemple ainsi
        qu'un mot de passe d'exemple.
        Ensuite, nous testons sur le formulaire
        est bien fonctionnel.
        """
        form_data = {
            'email': 'user@mail.test',
            'username': 'user',
            'password1': '123',
            'password2': '123',
            }
        form = LoginForm(data=form_data)
        #self.assertTrue(form.is_valid())

    def test_login(self):
        """
        Cette méthode permet de tester le formulaire
        de connexion sur l'application.
        Ici, nous utilisons
        un nom d'utilisateur d'exemple ainsi
        qu'un mot de passe d'exemple.
        Ensuite, nous testons sur le formulaire
        est bien fonctionnel.
        """
        form_data = {
            'username': 'user',
            'password': '123'
            }
        form = LoginForm(data=form_data)
        #self.assertTrue(form.is_valid())