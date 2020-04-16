from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_upload_path(instance, filename):
    return 'user-' + str(instance.seller.id) + '/' + filename

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

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    street1 = models.CharField(max_length=40)
    street2 = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    postal_code = models.PositiveIntegerField()
    phone_num = models.PositiveIntegerField()

class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    basket = models.PositiveIntegerField()
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    shipped = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    total_payment = models.DecimalField(max_digits=40,decimal_places=2)