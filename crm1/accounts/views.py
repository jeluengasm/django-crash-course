from django.shortcuts import render,redirect # We must use this function to render
from django.http import HttpResponse # Import library
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
from .filters import OrderFilter

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

def customer(request, pk_test):
    customer  = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()
    
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    
    context = {'customer': customer, 'orders': orders, 'order_count': order_count, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context) # First render

def createOrder(request, pk): # Create from Form request
    OrderFormSet = inlineformset_factory(Customer, Order, fields=("product","status"), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    # form = OrderForm(initial={'customer':customer})
    if request.method == 'POST':
        # print("Printing POST: ",request.POST)
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect("/")
    
    context = {'formset':formset}
    
    return render(request,'accounts/order_form.html', context)

def updateOrder(request,pk): # Update from Form request
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {'form':form}
    return render(request,'accounts/order_form.html', context)

def deleteOrder(request,pk): # Delete from Form request
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect("/")
    context = {'item':order}
    return render(request,'accounts/delete.html', context)