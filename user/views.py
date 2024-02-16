from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
# Create your views here.

def register(request):
    form = UserForm()
    if request.method =='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Başarılı bir şeklide kayıt oldunuz. Hoş geldiniz.')
            return redirect('index')
    context = {
        'form':form
    }
    return render (request, "register.html", context)

def userLogin(request):
    if request.method == 'POST':
        kullanici = request.POST.get('kullanici')
        sifre = request.POST.get('sifre')

        user = authenticate(request, username = kullanici, password = sifre)

        if user is not None:
            login(request, user)
            messages.success(request, 'Giriş Yapıldı')
            next = request.GET.get('next')
            if next:
                return redirect(next)
            else:
                return redirect('index')
        else:
            messages.error(request,"Kullanıcı adı vey şifre hatalı")
            print("Kullanıcı adı veya şifre hatalı")
            return redirect('login')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    messages.success(request, "Çıkış yaptınız. Yine Gel")
    return redirect('index')