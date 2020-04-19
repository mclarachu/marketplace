from django.urls import path, include
from . import views

app_name='profile'

urlpatterns = [
    path('add_product',views.add_product,name='add_product'),
    path('add_address',views.add_address,name='add_address'),
    path('<int:seller_id>/profile',views.profile,name='profile'),
    path('<int:prod_id>/product',views.product_detail,name='product_detail'),
    path('account', views.account, name='account')
]