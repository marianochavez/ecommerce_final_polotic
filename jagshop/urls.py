from io import IncrementalNewlineDecoder
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
    path('about/', views.about, name='about'),
    path('store/', include('store.urls'), name="store"),
    path('cart/', include('cart.urls'), name='cart'),
    # =========== USERs ==================
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/register/', views.signup, name='register'),
    path('account/', views.account, name='account'),
    path('account/modify/', views.accountModify, name='account_modify'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    # =========== contact ==================
    path('contact/', views.contactView, name='contact'),
    path('contact/success/', views.successContact, name='success'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
