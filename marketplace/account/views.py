from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Product,ShippingAddress
from . import forms
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def add_product(request):
    context = {}
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return HttpResponseRedirect(reverse('profile'))
        context['form'] = form
    return render(request,'account/add_product.html',context)

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
    return render(request,'account/shipping_address.html',context)

def profile(request,seller_id):
    items = Product.objects.filter(seller=seller_id)
    seller = get_object_or_404(User,pk=seller_id)
    context = {'items': items, 'seller': seller.username}
    return render(request, 'account/profile.html', context)



def product_detail(request,prod_id):
    item = Product.objects.get(pk=prod_id)
    context = {'item' : item}
    return render(request,'account/product_detail.html', context)





