from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from store.models import Product

from .forms import SignUpForm

def home(request):
    products = Product.objects.all().filter(is_active=True).order_by('-created')
    return render(request,'home.html',{'products': products})

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password1')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('home')
        else:
            form = SignUpForm()
        return render(request, 'registration/register.html', {'form': form})
    else:
        return redirect('home')