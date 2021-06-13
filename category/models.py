from django.db import models
from django.urls import reverse

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
