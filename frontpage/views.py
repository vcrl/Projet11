from django.shortcuts import render
from research.models import Product

# Create your views here.

def frontpage(request):
    return render(request, "frontpage/index.html")
    