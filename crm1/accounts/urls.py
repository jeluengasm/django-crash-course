"""crm1/accounts App URL Configuration"""

from django.urls import path
from . import views # Import the "views.py" file

urlpatterns = [
    path('', views.home, name="home"), # Write as a signal, no as a function or method!!!
    path('products/',views.products, name="products"),
    path('customer/<str:pk_test>',views.customer, name="customer"),
    
    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]