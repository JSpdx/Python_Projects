from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
#from .forms import ProductForm
# from .models import Product

def home(request):
    products = ["Cherries", "Apples", "Oranges", "Strawberries", "Pears", "Watermelons"]
    context = {
        'products': products,
    }
    return render(request, "home.html", context)
