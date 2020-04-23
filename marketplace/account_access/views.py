from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from . import forms
from profile.models import Basket,ItemBasket,Profile
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def signup(request):
    context = {}
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name']
                )
                user.profile.phone=form.cleaned_data['phone']
                user.save()
                #Create a basket for user
                newBasket = Basket(owner = user)
                newBasket.save()

                return HttpResponseRedirect(reverse('login'))
            except IntegrityError:
                form.add_error('username', 'Username is taken')

        context['form'] = form
    return render(request, 'account_access/signup.html', context)


def do_login(request):
    context = {}
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                user.profile.is_available=True
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect(reverse('store:index'))
            else:
                form.add_error(None, 'Incorrect username or password')
        context['form'] = form
    return render(request, 'account_access/login.html', context)


def do_logout(request):

    try:
        basket = Basket.objects.get(owner=request.user.id)
    except ObjectDoesNotExist:
        basket = Basket(owner=request.user)
        basket.save()

    #get all items reference
    items = ItemBasket.objects.filter(basket=basket)

    #add back to the item's inventory
    for item in items:
        item.item.inventory = item.item.inventory + item.count
        item.item.save()
        items.delete()

    #reset basket
    basket.totalAmount = 0
    basket.save()

    #make them not available
    request.user.profile.is_available = True
    logout(request)
    return HttpResponseRedirect(reverse('store:index'))
