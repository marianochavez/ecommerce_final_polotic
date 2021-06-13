from store.models import Product
from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_active=True)
    context = {
        'products': products
    }
    return render(request,'home.html',context)