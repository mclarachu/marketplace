from django.test import TestCase
from django.urls import reverse
from profile.models import Profile
from django.contrib.auth.models import User

class ModelTestCase(TestCase):

    def setUp(self):
        userTest = User.objects.create_user(username='test', password='test1234', email='test@mail.com')
        userTest.save()
        Profile.objects.create(user=userTest.username,phone='911',is_available='False')

    def test_profile_is_available(self):
        profileTest = self.client.get(username=userTest, phone='911')
        self.assertEquals(profileTest.is_available, 'False')













    #     class Profile(models.Model):
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    # phone = models.PositiveIntegerField(null=True)
    # is_available = models.BooleanField(default=False)

