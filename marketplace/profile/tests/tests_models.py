from django.test import TestCase
from django.urls import reverse
from profile.models import Profile
from django.contrib.auth.models import User

class ModelTestCase(TestCase):

    def setUp(self):
        userTest = User.objects.create_user(username='test', password='test1234', email='test@mail.com')
        userTest.save()
        userTest.profile.phone='911'
        userTest.save()

    def test_profile_is_available(self):
        userTest = User.objects.get(username='test')
        profileTest = Profile.objects.get(user=userTest, phone='911')
        self.assertFalse(profileTest.is_available)













    #     class Profile(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    # phone = models.PositiveIntegerField(null=True)
    # is_available = models.BooleanField(default=False)

