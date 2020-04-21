
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from .models import Product,ShippingAddress,Basket,OrderHistory,ItemBasket,ItemOrder
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

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
            return HttpResponseRedirect(reverse('account:account'))
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
def add_to_basket(request,item_id):
    prod = get_object_or_404(Product,pk=item_id)
    try:
        basket = Basket.objects.get(owner=request.user.id)
    except ObjectDoesNotExist:
        basket = Basket(owner=request.user)
        basket.save()
    if request.method=='POST':
        form = forms.AddToBasket(request.POST)
        if form.is_valid():
            ib = form.save(commit=False)
            ib.basket = basket
            ib.item = prod
            ib.save()

            #reduce one item from its inventory
            prod.inventory = prod.inventory - ib.count
            prod.save()

            #add price to basket
            basket.totalAmount += prod.price*ib.count
            basket.save()
            return HttpResponseRedirect(reverse('account:product_detail',kwargs={'prod_id':prod.id}))
    return render(request,'profile/product_detail.html',{'item': prod})

@login_required
def view_basket(request):
    try:
        basket = Basket.objects.get(owner=request.user.id)
    except ObjectDoesNotExist:
        basket = Basket(owner=request.user)
        basket.save()
    items = ItemBasket.objects.filter(basket=basket)
    return render(request,'profile/basket.html',{'items':items,'total':basket.totalAmount})

@login_required
def remove_from_basket(request,item_id):
    basket = get_object_or_404(Basket, owner=request.user.id)
    item = get_object_or_404(Product,pk=item_id)
    if request.method=='POST':
        ib = ItemBasket.objects.get(basket=basket,item=item)
        #add back into inventory
        item.inventory = item.inventory + ib.count
        item.save()

        #recalculate total amount
        basket.totalAmount -= item.price*ib.count
        basket.save()

        #delete item from basket
        ib.delete()
        items = ItemBasket.objects.filter(basket=basket)
        return HttpResponseRedirect(reverse('account:basket'))
    return render(request, 'profile/basket.html', {'items': items, 'total': basket.totalAmount})

@login_required
def checkout(request):
    basket = get_object_or_404(Basket,owner=request.user)
    list = ItemBasket.objects.filter(basket = basket)
    addresses = ShippingAddress.objects.filter(user=request.user)
    if request.method=='POST':
        address_id = request.POST['addressChoice']
        payment = request.POST['payment_option']
        address = get_object_or_404(ShippingAddress,pk=address_id)

        #Create an order instance to add to OrderHistory
        new_order = OrderHistory(
            user = request.user,
            shipped = address,
            total_payment = basket.totalAmount
        )
        new_order.save()

        for item in list:
            itemOrder = ItemOrder(
                order = new_order,
                item = item.item,
                count = item.count
            )
            itemOrder.save()

        #delete the current basket
        basket.delete()

        return HttpResponseRedirect(reverse('account:orderSummary',kwargs={'order_id':new_order.id}))
    return render(request,'profile/checkout.html',{'list':list,'total':basket.totalAmount,'addresses':addresses})

@login_required
def add_address2(request):
    context = {}
    if request.method == 'POST':
        form = forms.AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = request.user
            address.save()
            return HttpResponseRedirect(reverse('account:checkout'))
        context['form'] = form
    return render(request, 'profile/shipping_address.html', context)

def orderSummary(request,order_id):
    order = get_object_or_404(OrderHistory,pk=order_id)
    list = ItemOrder.objects.filter(order=order)
    return render(request,'profile/orderSummary.html', {'order':order,'list':list})
