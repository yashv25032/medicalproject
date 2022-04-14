from django.db import models

# Create your models here.
class Dealer(models.Model):
    dname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.CharField(max_length=50)


class Employee(models.Model):
    empid = models.IntegerField(unique=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    salary = models.PositiveBigIntegerField(unique=True)
    phn_no = models.PositiveBigIntegerField(unique=True)

class Customer(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    phn_no = models.BigIntegerField()
    email = models.CharField(max_length=50)

class Medicine(models.Model):
    m_id = models.IntegerField(unique=True)
    mname = models.CharField(max_length=30)
    dname = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    price = models.CharField(max_length=30)
    stock = models.IntegerField()

class Purchase(models.Model):
    pname = models.CharField(max_length=30)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    phn_no = models.BigIntegerField()
    price = models.BigIntegerField()
    qty = models.BigIntegerField()
    total = models.BigIntegerField()


       

    

            