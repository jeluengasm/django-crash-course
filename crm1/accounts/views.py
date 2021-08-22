from django.shortcuts import render
from django.http import HttpResponse # Import library

# Create your views here.

## Create functions in the view's file

def home(request):
    return HttpResponse('home')

def products(request):
    return HttpResponse('products')

def customer(request):
    return HttpResponse('customer')