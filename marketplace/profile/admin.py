from django.contrib import admin
from .models import Product,Basket,ShippingAddress,OrderHistory
# Register your models here.
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(ShippingAddress)
admin.site.register(OrderHistory)