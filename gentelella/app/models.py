from __future__ import unicode_literals

from django.db import models

# Create your models here.
NAME_MAX_LENGTH = 50

class Supplier(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=NAME_MAX_LENGTH)
    legal_person = models.CharField(max_length=NAME_MAX_LENGTH)
    account = models.CharField(max_length=30)

class Member(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    phone = models.CharField(max_length=11)
    credits = models.IntegerField()

class Contract(models.Model):
    supplier = models.IntegerField()
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    price = models.IntegerField()
    cost = models.IntegerField()
    sales_return = models.IntegerField()
    complimentary = models.CharField(max_length=NAME_MAX_LENGTH, default="")
    create_time = models.DateTimeField(auto_now_add=True )

class Indent(models.Model):
    contract = models.IntegerField()
    number = models.IntegerField()
    date = models.DateTimeField()
    style = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

class PriceFile(models.Model):
    contract = models.IntegerField()
    min_price = models.IntegerField()
    max_price = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

class Record(models.Model):
    supplier = models.IntegerField()
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=NAME_MAX_LENGTH)
    create_time = models.DateTimeField(auto_now_add=True)

class TempRecord(models.Model):
    contract = models.IntegerField()
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=NAME_MAX_LENGTH)
    create_time = models.DateTimeField(auto_now_add=True)

class SalesRecord(models.Model):
    supplier = models.IntegerField()
    member = models.IntegerField()
    pricefile = models.IntegerField()
    supplier_discount = models.IntegerField()
    company_discount = models.IntegerField()
    address = models.CharField(max_length=NAME_MAX_LENGTH)
    create_time = models.DateTimeField(auto_now_add=True)

class GoodsRecord(models.Model):
    record = models.IntegerField()
    temprecord = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)