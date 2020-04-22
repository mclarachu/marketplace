from django.test import TestCase
from . import views
# Create your tests here.
#test signing up
class SignUpTest(TestCase):

    #test views
    def test_sign_up_view(self):
        resp = self.client.get('signup')
        self.assertEqual(resp.status_code,200)


#test log in

#test that before login, some tabs are not available.

