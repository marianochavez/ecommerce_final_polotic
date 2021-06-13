from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','is_active','stock','created')
    search_fields = ('title','slug','description','category')
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Product, ProductAdmin)