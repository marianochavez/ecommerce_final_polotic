from django.urls import path
from .views import store, product_detail, search, product_create, product_edit, product_delete

urlpatterns = [
    path('', store, name='store'),
    path("category/<slug:category_slug>/", store, name="products_by_category"),
    path("category/<slug:category_slug>/<slug:product_slug>/", product_detail, name="product_detail"),
    path('search/', search, name='search'),
    path('product_create/', product_create, name='product_create'),
    path('product_edit/<slug:product_slug>/', product_edit, name='product_edit'),
    path('product_delete/<slug:product_slug>/', product_delete, name='product_delete'),
    
]

