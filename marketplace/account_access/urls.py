from django.urls import path, include

from . import views

urlpatterns = [
    path('market', views.info, name='acc_info'),
    path('market', views.market, name='market'),
    path('signup', views.signup, name='signup'),
    path('login', views.do_login, name='login'),
    path('logout', views.do_logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('store', views.show_store, name='store'),
]