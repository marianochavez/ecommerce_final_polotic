from store.models import Product
from django.shortcuts import render
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_active=True).order_by('-created')
    context = {
        'products': products
    }
    return render(request,'home.html',context)