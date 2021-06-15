from django.urls.conf import include
from jagshop import settings
from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('store/', include('store.urls'), name="store"),
    path('cart/', include('cart.urls'), name='cart'),
    # =========== USERs ==================
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/register/', views.signup, name='registro'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
