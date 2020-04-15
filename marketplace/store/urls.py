from django.urls import path
import store.views

urlpatterns = [
    path('', store.views.index, name='index'),
]