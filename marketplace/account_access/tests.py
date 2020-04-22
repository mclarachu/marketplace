from django.test import TestCase
from . import views
from django.urls import reverse
from .forms import SignupForm
from selenium import webdriver
# Create your tests here.
#test signing up
class SignUpTest(TestCase):

    #test views
    def test_sign_up_view(self):
        resp = self.client.get(reverse('signup'))
        self.assertEqual(resp.status_code,200)

    #test sign up form
    def test_valid_sign_up_form(self):
        data = {'username':'testing', 'first_name':'test', 'last_name':'er', 'email':'test@test.com','phone':328929329,
                'password':'testing123','password_confirm':'testing123'}
        form = SignupForm(data=data)
        self.assertTrue(form.is_valid())

    #password is too short
    def test_invalid_sign_up_form(self):
        data = {'username': 'testing2', 'first_name': 'test', 'last_name': 'er', 'email': 'test2@test.com',
                'phone': 328929329,'password': 'test4', 'password_confirm': 'test4'}
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())

#test authenticated and non_authenticated views
class UserAuthenticationViewTest(TestCase):


#test that before login, some tabs are not available.

