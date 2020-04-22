from django.test import TestCase
from django.urls import reverse
from profile.forms import AddressForm,AddToBasket

class TestIndex(TestCase):

    def test_invalid_address_missing_province(self):
        data = {'country': 'Canada', 'street1': '121 Spring Drive',
                'street2': '#2793', 'city': 'Toronto',
                'province': '', 'postal_code': '123 123'}
        form = AddressForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_address(self):
        data = {'country': 'Canada', 'street1': '121 Spring Drive',
                'street2': '#2793', 'city': 'Toronto',
                'province': 'Ontario', 'postal_code': '123 123'}
        form = AddressForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_address_without_street2(self):
        data = {'country': 'Canada', 'street1': '121 Spring Drive',
                'street2': '', 'city': 'Toronto',
                'province': 'Ontario', 'postal_code': '123 123'}
        form = AddressForm(data=data)
        self.assertTrue(form.is_valid())

    def test_valid_add_to_basket(self):
        data = {'count': '2'}
        form = AddToBasket(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_add_to_basket(self):
        data = {'count': '-4'}
        form = AddToBasket(data=data)
        self.assertFalse(form.is_valid())


