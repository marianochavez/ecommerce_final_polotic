from django.contrib.auth import authenticate, login
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from store.models import Product

from .forms import ContactForm, SignUpForm
from django.contrib.auth.models import User

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

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['rocodoko21@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    return render(request, "contact.html", {'form': form})

def successView(request):
    return render(request,'contact.html',{'sended':'Gracias por contactarnos!'})

def about(request):
    return render(request,'about.html')