from django.test import TestCase
from . import views
from django.urls import reverse
from .forms import SignupForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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
    def test_invalid_password(self):
        data = {'username': 'testing', 'first_name': 'test', 'last_name': 'er', 'email': 'test@test.com',
                'phone': 328929329,'password': 'test4', 'password_confirm': 'test4'}
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())

    # password contains only alphabets
    def test_invalid_password_alpha(self):
        data = {'username': 'testing', 'first_name': 'test', 'last_name': 'er', 'email': 'test@test.com',
                'phone': 328929329, 'password': 'wrongalpha', 'password_confirm': 'wrongalpha'}
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())

    # password contains only numbers
    def test_invalid_password_digits(self):
        data = {'username': 'testing', 'first_name': 'test', 'last_name': 'er', 'email': 'test@test.com',
                'phone': 328929329, 'password': '123456789', 'password_confirm': '123456789'}
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_email(self):
        data = {'username': 'testing', 'first_name': 'test', 'last_name': 'er', 'email': 'test@test',
                'phone': 328929329, 'password': 'testing123', 'password_confirm': 'testing123'}
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_phone_number(self):
        data = {'username': 'testing', 'first_name': 'test', 'last_name': 'er', 'email': 'test@test',
                'phone': 'invalid', 'password': 'testing123', 'password_confirm': 'testing123'}
        form = SignupForm(data=data)
        self.assertFalse(form.is_valid())

#Test Login
class LogInTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='test1234', email='test@mail.com')
        self.user.save()

    def tearDown(self):
         self.user.delete()

    def test_login_form(self):
        data = {'username':self.user.username,'password':self.user.password}
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

    def test_correct_login(self):
        user = authenticate(username='test',password='test1234')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='test1234')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse((user is not None) and user.is_authenticated)


