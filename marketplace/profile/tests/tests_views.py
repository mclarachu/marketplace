from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from profile.models import ShippingAddress

class TestAccountView(TestCase):

    def setUp(self):
        user1 = User.objects.create_user\
            (username='test',
             password='test1234',
             email='test@mail.com',
             first_name='test1',
             last_name='test2')
        user1.save()
        login = self.client.login(username='test', password='test1234')

    def test_account_view_render(self):
        response = self.client.get(reverse('account:account'))
        self.assertEqual(str(response.context['user']), 'test')
        self.assertEqual(response.status_code, 200)

    def test_account_username(self):
        response = self.client.get(reverse('account:account'))
        self.assertContains(response, 'Full name: test1 test2')

    def test_account_address(self):
        response = self.client.get(reverse('account:account'))
        self.assertEqual(str(response.context['addresses']),'<QuerySet []>')

    def test_account_with_address(self):
        response = self.client.get(reverse('account:account'))
        address1 = ShippingAddress\
            (user = response.context['user'],
                 country = 'Canada',
                 street1 = '121 Spring Drive',
                 street2 = '#2793',
                 city= 'Toronto',
                 province= 'Ontario',
                 postal_code= '123 123'
            )
        address1.save()
        response = self.client.get(reverse('account:account'))
        self.assertContains(response, 'Canada')
        self.assertContains(response,'121 Spring Drive')
        self.assertContains(response, '#2793')






