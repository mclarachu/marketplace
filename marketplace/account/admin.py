from django.contrib import admin
from account.models import *

# Register your models here.
admin.site.register(Basket)
admin.site.register(Product)
admin.site.register(ShippingAddress)
admin.site.register(OrderHistory)