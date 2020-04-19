from django.urls import path, include

from . import views

urlpatterns = [
    path('market', views.info, name='acc_info'),
    path('signup', views.signup, name='signup'),
    path('login', views.do_login, name='login'),
    path('logout', views.do_logout, name='logout'),
]