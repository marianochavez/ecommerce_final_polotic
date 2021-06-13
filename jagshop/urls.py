from django.urls.conf import include
from jagshop import settings
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('store/', include('store.urls'), name="store"),
    path('cart/', include('cart.urls'), name='cart'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
