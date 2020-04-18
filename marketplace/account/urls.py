from django.urls import path, include
from . import views

urlpatterns = [
    path('add_product',views.add_product,name='add_product'),
    path('add_address',views.add_address,name='add_address'),
    #path(r'^(?P<userid>[0-9]+)$',views.profile,name='profile'),
]