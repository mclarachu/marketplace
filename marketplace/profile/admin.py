from django.contrib import admin
from .models import Product,Basket,ShippingAddress,OrderHistory,ItemBasket,ItemOrder,Profile
# Register your models here.
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(ShippingAddress)
admin.site.register(OrderHistory)
admin.site.register(ItemBasket)
admin.site.register(ItemOrder)
admin.site.register(Profile)