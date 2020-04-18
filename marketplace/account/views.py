from django.shortcuts import render
from .models import Product, ShippingAddress
from . import forms
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def add_product(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return HttpResponseRedirect(reverse('profile'))
        context['form'] = form
    return render(request, 'account/product_details.html', context)


@login_required
def add_address(request):
    context = {}
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return HttpResponseRedirect(reverse('profile'))
        context['form'] = form
    return render(request, 'account/shipping_address.html', context)
