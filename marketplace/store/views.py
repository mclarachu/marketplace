from django.shortcuts import render
from django.http import HttpResponse
from account.models import Product


def index(request):
    #return HttpResponse('<h1>heyya</h1>')
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request,'store/index.html',context)

# Create your views here.
