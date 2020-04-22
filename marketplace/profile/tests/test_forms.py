from django.test import TestCase
from . import views
from django.urls import reverse
from .forms import AddressForm
from selenium import webdriver

def test_invalid_address_form(self):
    data = {'country': '', 'street1': '121 Spring Drive',
            'street2': '#2793', 'city': 'Toronto',
            'province': 'Ontario', 'postal_code': '123 123'}
    form = AddressForm(data=data)
    self.assertFalse(form.is_valid())

    # class AddressForm(ModelForm):
    #     class Meta:
    #         model = ShippingAddress
    #         fields = ['country','street1','street2','city','province','postal_code']

