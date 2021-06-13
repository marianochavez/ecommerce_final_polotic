from django.urls import path
from .views import add_cart, remove_cart, cart, remove_cart_item,remove_all_cart_items

urlpatterns = [
    path('', cart, name='cart'),
    path('add_cart/<int:product_id>/', add_cart, name='add_cart'),
    path('remove_cart/<int:product_id>/', remove_cart, name='remove_cart'),
    path('remove_cart_item/<int:product_id>/', remove_cart_item, name='remove_cart_item'),
    path('remove_all_cart_items/', remove_all_cart_items, name='remove_all_cart_items'),
]
