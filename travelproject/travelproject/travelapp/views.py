from django.shortcuts import render
from django.http import HttpResponse
from .models import place,news
# Create your views here.

def index(request):
    obj = place.objects.all()
    n = news.objects.all()
    print(n)
    print(obj)
    context={'object':obj,
             'news':n}
    return render(request, 'index.html',context)
def demo(request):
    return render(request,'demo.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')