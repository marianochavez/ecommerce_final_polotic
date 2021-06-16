from django.contrib import admin
from .models import Product,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug','is_active','created')
    search_fields =  ('name','slug')
    prepopulated_fields = {'slug': ('name',)}



class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','category','is_active','stock','created')
    search_fields = ('title','slug','description','category')
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)  