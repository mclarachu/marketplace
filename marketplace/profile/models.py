from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator

# Create your models here.
def validate_price(value):
    if value>=0:
        return value
    else:
        raise ValidationError("Price must be a positive value")

def get_upload_path(instance, filename):
    return 'user-' + str(instance.seller.id) + '/' + filename

class Product(models.Model):
    seller = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to=get_upload_path)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=19,decimal_places=2,validators=[validate_price])
    inventory = models.PositiveIntegerField()

    def __str__(self):
        return self.seller.username + ' - ' + self.name

class Basket(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    totalAmount=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.owner.username

class ItemBasket(models.Model):
    basket = models.ForeignKey(Basket,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField()

    def __str__(self):
        return self.basket.owner.username +' : ' + self.item.name

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=40)
    street1 = models.CharField(max_length=40)
    street2 = models.CharField(max_length=40,blank=True)
    city = models.CharField(max_length=40)
    province = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=10)
    phone_num = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username

class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
    shipped = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    total_payment = models.DecimalField(max_digits=40,decimal_places=2)

    def __str__(self):
        return self.user.username