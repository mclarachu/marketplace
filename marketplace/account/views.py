from django.shortcuts import render
from .models import Product,ShippingAddress
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_product(request):
    context = {}

def add_address(request):
    context = {}
