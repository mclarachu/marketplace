from django import forms
from django.forms import ModelForm
from django.core.validators import MinValueValidator
from .models import Product, ShippingAddress

class AddressForm(forms.Form):
    class Meta:
        model = ShippingAddress
        fields = ['fullname','country','street1','street2','city','province','postal_code','phone_num']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','image','description','price','inventory']