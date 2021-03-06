from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product

from .models import Cart, CartItem


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

@login_required(login_url='/accounts/login/')
def cart(request, total=0, quantity=0, cart_items=None):
    shipping = 0
    grand_total = 0
    try:
        cart = Cart.objects.get(user = request.user, is_open = True)
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            quantity += cart_item.quantity
        shipping = 600
        grand_total = total + shipping

    except ObjectDoesNotExist:
        pass

    context = {
        'total':total,
        'quantity':quantity,
        'cart_items': cart_items,
        'shipping': shipping,
        'grand_total': grand_total,
    }
    return render(request, 'store/cart.html', context)

@login_required(login_url='/accounts/login/')
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(user=request.user, is_open=True)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id = _cart_id(request), user = request.user)
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')

@login_required(login_url='/accounts/login/')
def remove_cart(request, product_id):
    cart = Cart.objects.get(user = request.user, is_open = True)
    product = get_object_or_404(Product, id = product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart')

@login_required(login_url='/accounts/login/')
def remove_cart_item(request, product_id):
    cart = Cart.objects.get(user = request.user, is_open = True)
    product = get_object_or_404(Product, id = product_id)
    cart_item = CartItem.objects.get(product = product, cart = cart)
    cart_item.delete()
    return redirect('cart')

@login_required(login_url='/accounts/login/')
def remove_all_cart_items(request):
    cart = Cart.objects.get(user = request.user, is_open = True)
    cart_item = CartItem.objects.all().filter(cart = cart)
    cart_item.delete()
    return redirect('cart')