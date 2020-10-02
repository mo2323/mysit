from django.shortcuts import render
from products.models import Product
def index(requset):
    context = {
        'products': Product.objects.all()
    }
    return render(requset, 'pages/index.html', context)
def about(request):
    return render(request, 'pages/about.html')
def coffee(request):
    return render(request, 'pages/coffee.html')
def mostafa(request):
    return render(request, 'pages/mostafa.html')