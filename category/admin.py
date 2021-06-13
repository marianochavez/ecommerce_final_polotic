from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug','is_active','created')
    search_fields =  ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category,CategoryAdmin)