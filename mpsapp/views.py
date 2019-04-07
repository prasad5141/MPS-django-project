# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from django.shortcuts import redirect

# Create your views here.
def home(request):
    if request.method == "GET":
        items = ItemPost.objects.all().order_by('timestamp')

    return render(request, 'home.html', {'items':items} )


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = RegistrationForm()
            return redirect('registration')
    else:
        form = RegistrationForm()
        return render(request, 'registration.html', {'form':form})

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
           un = request.POST.get('username')
           pwd = request.POST.get('password')
           dbuser = Registration.objects.filter(username=un, password=pwd)
           if not dbuser:
              return HttpResponse("Login Failed")
           else:
               return redirect('home')
        else:
            form = LoginForm(request.POST)
            return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        return render(request, 'login.html', {'form': form})


def shopkeeper(request):
    if request.method == 'POST':
        form = ShopkeeperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ShopkeeperForm()
            return render(request, 'shopkeeper.html', {'form':form})
    else:
        form = ShopkeeperForm()
        return render(request, 'shopkeeper.html', {'form': form})



def shopkeeperlogin(request):
    if request.method == "POST":
        form = ShopkeeperLoginForm(request.POST)
        if form.is_valid():
           un = request.POST.get('username')
           pwd = request.POST.get('password')
           dbuser = Shopkeeper.objects.filter(username=un, password=pwd)
           if not dbuser:
              return HttpResponse("Login Failed")
           else:
               return redirect('itempost')
        else:
            form = ShopkeeperLoginForm(request.POST)
            return render(request, 'shopkeeperlogin.html', {'form': form})
    else:
        form = ShopkeeperLoginForm(request.POST)
        return render(request, 'shopkeeperlogin.html', {'form': form})



def itempost(request):
    if request.method == "POST":
        form = ItemPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = ItemPostForm()
            return render(request, 'itempost.html', {'form':form})
    else:
        form = ItemPostForm()
        return render(request, 'itempost.html', {'form':form})


def billing(request, item_id):
    bill_item = ItemPost.objects.get(id=item_id)
    actual_price = bill_item.medicineprice
    discount = 10
    payable_price = actual_price-actual_price*discount/100
    form = Payment_mode()
    return render(request, 'billing.html', {'bill_item':bill_item, 'payable_price':payable_price, 'discount':discount, 'form':form})


def pay(request):
    if request.method == "POST":
        form = BillingForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Your Order Confirmed<h1>')
        else:
            form = BillingForm()
            return render(request, 'pay.html', {'form':form})
    else:
        form = BillingForm()
        return render(request, 'pay.html',{'form':form})

