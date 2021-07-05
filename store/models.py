from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    slug = models.SlugField()
    is_active = models.BooleanField(default=True)
    created = models.DateField(auto_now=False,auto_now_add=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('products_by_category', args = [self.slug])

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = RichTextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='products',default='default_prod.jpg')
    image_link = models.URLField(default='https://i.imgur.com/dQpzDHi.jpg')
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