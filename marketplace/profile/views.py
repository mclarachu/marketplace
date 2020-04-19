
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Product,ShippingAddress
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

from . import forms

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def account(request):
    address = ShippingAddress.objects.filter(user=request.user.id)
    return render(request,'profile/account.html',{'addresses':address})

@login_required
def add_product(request):
    context = {}
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            return HttpResponseRedirect(reverse('account:profile',kwargs={'seller_id': request.user.id}))
        context['form'] = form
    return render(request,'profile/add_product.html',context)

@login_required
def add_address(request):
    context = {}
    if request.method == 'POST':
        form = forms.AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return HttpResponseRedirect(reverse('account'))
        context['form'] = form
    return render(request, 'profile/shipping_address.html', context)

def profile(request,seller_id):
    items = Product.objects.filter(seller=seller_id)
    seller = get_object_or_404(User,pk=seller_id)
    context = {'items': items, 'seller': seller}
    return render(request, 'profile/profile.html', context)

def product_detail(request,prod_id):
    item = Product.objects.get(pk=prod_id)
    context = {'item' : item}
    return render(request,'profile/product_detail.html', context)

@login_required
def delete_address(request,address_id):
    address = get_object_or_404(ShippingAddress,pk=address_id)
    address.delete()
    address = ShippingAddress.objects.filter(user=request.user.id)
    return render(request,'profile/account.html',{'addresses':address})

@login_required
def delete_item(request,item_id):
    item = get_object_or_404(Product,pk=product_id)
    item.delete()
    item = product_list.objects.filter(seller=request.user.id)
    return render(request,'profile/profile.html',{'items': item,'seller':request.user.username})

@login_required
def add_to_basket(request,item_id,num):

    item = Basket(
        user = request.user.id,
        item = item_id,
        amount = num
    )

