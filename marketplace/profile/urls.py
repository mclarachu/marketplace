from django.urls import path, include
from . import views
app_name='account'
urlpatterns = [

    path('<int:seller_id>',views.profile,name='profile'),
    path('<int:prod_id>/product/',views.product_detail,name='product_detail'),
    path('add_product',views.add_product,name='add_product'),
    path('add_address',views.add_address,name='add_address'),
    path('add_address2',views.add_address2,name='add_address2'),
    path('account', views.account, name='account'),
    path('basket',views.view_basket,name='basket'),
    path('<int:item_id>/addToBasket/',views.add_to_basket,name='add_to_basket'),
    path('<int:item_id>/removeBasket/',views.remove_from_basket,name='remove_from_basket'),
    path('checkout',views.checkout,name='checkout'),
    path('<int:order_id>/orderSummary/',views.orderSummary,name='orderSummary'),
    path('orderHistory',views.orderHistory,name='orderHistory'),
    path('<int:item_id>/updateProduct/',views.updateProduct,name='updateProduct'),
    path('<int:address_id>/updateAddress/',views.updateAddress,name='updateAddress'),
    path('<int:item_id>/deleteItem/',views.deleteItem,name='deleteItem'),
]