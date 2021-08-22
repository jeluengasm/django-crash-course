from django.shortcuts import render # We must use this function to render
from django.http import HttpResponse # Import library

# Create your views here.

## Create functions in the view's file

def home(request):
    return render(request, 'accounts/dashboard.html') # First render

def products(request):
    return render(request, 'accounts/products.html') # First render

def customer(request):
    return render(request, 'accounts/customers.html') # First render