from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from product.models import Product

def index(request):
    products = Product.objects.all()
    
    return render(request, 'index.html', {'products':products})