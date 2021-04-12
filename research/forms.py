"""
Formulaires de l'application 'accounts'
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RatingForm(forms.Form):
    FILTER_CHOICES = (
        ('1', '⭐️'),
        ('2', '⭐️⭐️'),
        ('3', '⭐️⭐️⭐️'),
        ('4', '⭐️⭐️⭐️⭐️'),
        ('5', '⭐️⭐️⭐️⭐️⭐️')
    )

    rating = forms.ChoiceField(choices = FILTER_CHOICES)