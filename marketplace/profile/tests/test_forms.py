from django.test import TestCase
from django.urls import reverse
from profile.forms import AddressForm,AddToBasket, ProductForm

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

    def test_valid_product(self):
        data = {'seller': '1', 'name': 'dog', 'image':'testPath',
                'description': '12 weeks puppy, vaccinated',
                'price':'2300', 'inventory':'4'}
        form = ProductForm(data=data)
        self.assertTrue(form.is_valid())

    # class Product(models.Model):
    #     seller = models.ForeignKey(User,on_delete=models.CASCADE)
    # name = models.CharField(max_length=30)
    # image = models.FileField(upload_to=get_upload_path)
    # description = models.CharField(max_length=1000)
    # price = models.DecimalField(max_digits=19,decimal_places=2,validators=[validate_price])
    # inventory = models.PositiveIntegerField()







