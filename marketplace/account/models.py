from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_upload_path(instance, filename):
    return 'user-' + str(instance.owner.id) + '/' + filename

class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to=get_upload_path)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=19,decimal_places=2)
    inventory = models.PositiveIntegerField()

class Basket(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

class shippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

