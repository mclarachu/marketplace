from django.test import TestCase
from . import views
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.
class TestIndex (TestCase):

    def setUp(self):
        user1 = User.objects.create_user(username='test', password='test1234', email='test@mail.com')
        user1.save()

    def test_anonymous_index_view(self):
        response = self.client.get(reverse('store:index'))
        # check if response was a success
        self.assertEqual(response.status_code, 200)

        self.assertContains(response,'id="index"')
        self.assertContains(response, 'id="chat"')
        self.assertContains(response, 'id="signup"')
        self.assertContains(response, 'id="login"')

    def test_logged_in_index_view(self):
        login = self.client.login(username='test',password='test1234')
        response = self.client.get(reverse('store:index'))

        #check if user is logged in
        self.assertEqual(str(response.context['user']), 'test')

        #check if response was a success
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'id="index"')
        self.assertContains(response, 'id="chat"')
        self.assertContains(response, 'id="basket"')
        self.assertContains(response, 'id="profile"')
        self.assertContains(response, 'id="account"')
        self.assertContains(response, 'id="logout"')



