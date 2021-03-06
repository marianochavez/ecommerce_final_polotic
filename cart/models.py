from django.db import models
from store.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_id = models.CharField(max_length=250,blank=True)
    created = models.DateField(auto_now=False, auto_now_add=True)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return (self.product.price * self.quantity)

    def __unicode__(self):
        return self.product