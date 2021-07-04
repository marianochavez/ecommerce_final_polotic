from django.urls.base import is_valid_path
from store.forms import ProductForm
from cart.models import CartItem
from cart.views import _cart_id
from django.core import paginator
from django.core.paginator import EmptyPage, Page, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages 
from store.models import Product, Category
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test
import operator


def store(request,category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = categories, is_active = True)
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_active=True).order_by('id')
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
        product_count = products.count()

    context = {
        'products': paged_products,
        'product_count':product_count,
        'category':categories,
    }
    return render(request,'store/store.html',context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug = category_slug, slug = product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id = _cart_id(request), product = single_product).exists()

    except Exception as e:
        raise e

    context = {
        'single_product':single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html',context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword != '':
            products = Product.objects.order_by('-created').filter(Q(description__icontains = keyword) | Q(title__icontains = keyword),is_active=True)
            product_count = products.count()

    context = {
        'products':products,
        'product_count': product_count,
        'keyword': keyword,
    }
    return render(request, 'store/store.html', context)

@staff_member_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
            
    return render(request,'store/product_create.html', {'form': form})

@user_passes_test(operator.attrgetter('is_staff'), login_url='home')
def product_edit(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    if request.method == 'POST':
        form = ProductForm(data=request.POST,files=request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
           return render(request,'store/product_edit.html', {'form': form, 'product':product})
    else:
        form = ProductForm(instance=product)
        return render(request,'store/product_edit.html', {'form': form, 'product':product})

@staff_member_required
def product_delete(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    product.is_active = False
    product.save()
    return redirect('home')