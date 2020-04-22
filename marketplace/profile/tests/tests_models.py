from django.test import TestCase
from django.urls import reverse
from profile.models import Profile, Basket, ShippingAddress, OrderHistory
from django.contrib.auth.models import User


class ModelTestCase(TestCase):

    def setUp(self):
        userTest = User.objects.create_user(username='test', password='test1234', email='test@mail.com')
        userTest.save()

    def test_profile_is_available(self):
        userTest = User.objects.get(username='test')
        profileTest = Profile.objects.get(user=userTest)
        self.assertFalse(profileTest.is_available)

    def test_basket_total_amount(self):
        userTest = User.objects.get(username='test')
        basketTest = Basket.objects.create(owner=userTest)
        self.assertEquals(basketTest.totalAmount, 0)

    def test_shipping_address(self):
        userTest = User.objects.get(username='test')
        shipAdd = ShippingAddress.objects.create(user=userTest,country='Canada',street1='121 Spring Drive',city='TO',province='ON',postal_code='M2N 7F2')
        self.assertEquals(shipAdd.country, 'Canada')

    def test_order_history(self):
        userTest = User.objects.get(username='test')
        shipAdd = ShippingAddress.objects.create(user=userTest,country='Canada',street1='121 Spring Drive',city='TO',province='ON',postal_code='M2N 7F2')
        orderHis = OrderHistory.objects.create(user=userTest, shipped=shipAdd,total_payment='30')
        self.assertEquals(orderHis.shipped.country, 'Canada')