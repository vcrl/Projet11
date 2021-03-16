from ..forms import SignUpForm, LoginForm
from django.test import TestCase, Client
from django.contrib.auth.models import User

class Test_Forms(TestCase):
    def init(self):
        self.client = Client()

    def test_signup(self):
        form_data = {
            'email': 'user@mail.test',
            'username': 'user',
            'password1': '123',
            'password2': '123',
            }
        form = LoginForm(data=form_data)
        #self.assertTrue(form.is_valid())

    def test_login(self):
        form_data = {
            'username': 'user',
            'password': '123'
            }
        form = LoginForm(data=form_data)
        #self.assertTrue(form.is_valid())