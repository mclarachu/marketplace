from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
def validate_price(value):
    if value>=0:
        return value
    else:
        raise ValidationError("Price must be a positive value")

def get_upload_path(instance, filename):
    return 'user-' + str(instance.seller.id) + '/' + filename

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.PositiveIntegerField(null=True)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

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
    totalAmount=models.DecimalField(max_digits=19,decimal_places=2,validators=[validate_price],default=0)

    def __str__(self):
        return self.owner.username

class ItemBasket(models.Model):
    basket = models.ForeignKey(Basket,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

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

    def __str__(self):
        return self.user.username

class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shipped = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    total_payment = models.DecimalField(max_digits=40,decimal_places=2,default=0)
    dateTime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

class ItemOrder(models.Model):
    order = models.ForeignKey(OrderHistory,on_delete=models.CASCADE)
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.order.user.username +' : ' + self.item.name