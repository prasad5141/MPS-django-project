  # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=30)
    email    = models.EmailField()
    password = models.CharField(max_length=30)


class Shopkeeper(models.Model):
    username = models.CharField(max_length=30)
    email    = models.EmailField()
    password = models.CharField(max_length=30)
    shopname = models.CharField(max_length=30)
    shopaddress = models.CharField(max_length=30)


class ItemPost(models.Model):
    medicineprice = models.DecimalField(decimal_places=2,max_digits=20,default=9.99)
    medicineName = models.CharField(max_length=30)
    manfacturerName = models.CharField(max_length=30,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Billing(models.Model):
    cardNo = models.IntegerField()
    cvv    = models.IntegerField()
    expiryDate = models.DateField()
    cardHolderName = models.CharField(max_length=30)
