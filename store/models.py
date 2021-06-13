from django.db.models.deletion import CASCADE
from category.models import Category
from django.db import models
from django.urls import reverse

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=500,blank=False)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products',default='default_prod.jpg')
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    stock = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.title  

    def get_url(self):
        return reverse('product_detail', args = [self.category.slug, self.slug])