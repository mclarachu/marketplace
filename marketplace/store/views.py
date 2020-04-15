from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #return HttpResponse('<h1>heyya</h1>')
    return render(request,'store/index.html',{})

# Create your views here.
