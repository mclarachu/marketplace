from django import forms
from django.forms import ModelForm
from django.core.validators import MinValueValidator
from .models import Product, ShippingAddress, ItemBasket

class AddressForm(ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['country','street1','street2','city','province','postal_code','phone_num']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','description','price','inventory']

class AddToBasket(ModelForm):
    class Meta:
        model = ItemBasket
        fields =['count']

class Checkout(forms.Form):
    creditcard = forms.CharField()
    address = forms.IntegerField()