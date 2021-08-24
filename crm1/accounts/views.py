from django.shortcuts import render # We must use this function to render
from django.http import HttpResponse # Import library
from .models import *

# Create your views here.

## Create functions in the view's file

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    
    total_customers = customers.count()
    total_orders = orders.count()
    
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()
    
    context = {'orders': orders, 'customers': customers,
               'total_customers': total_customers, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    
    return render(request, 'accounts/dashboard.html', context) # First render

def products(request):
    products = Product.objects.all()
    
    return render(request, 'accounts/products.html', {'products': products}) # First render

def customer(request):
    return render(request, 'accounts/customers.html') # First render