"""MPS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mpsapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url('registration/', views.registration, name='registration'),
    url('login/', views.login, name='login'),
    url('shopkeeper/', views.shopkeeper, name='shopkeeper'),
    url('shopkeeperlogin/', views.shopkeeperlogin, name='shopkeeperlogin'),
    url('itempost/', views.itempost, name='itempost'),
    #url('itemview/', views.itemview, name='itemview'),
    url('billing/(\d{1,})' , views.billing, name='billing'),
    url('pay/', views.pay, name='pay')
]
