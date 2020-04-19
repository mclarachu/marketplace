from django.urls import path, include
from . import views
app_name='account'
urlpatterns = [

    path('<int:seller_id>',views.profile,name='profile'),
    path('product/<int:prod_id>',views.product_detail,name='product_detail'),
    path('add_product',views.add_product,name='add_product'),
    path('add_address',views.add_address,name='add_address'),
    path('account', views.account, name='account'),
    path('basket',views.view_basket,name='basket')
]