from django import forms
from .models import Dealer, Employee
from .models import Customer
from .models import Medicine
from .models import Purchase

class dealerform(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ['dname','address','phone','email']
        labels = {
            'dname':'Dealername','address' :'Address','phone':'Phone','email':'Email'
        }

        widgets = {
            'dname': forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['empid','fname','lname','address','email','salary','phn_no']
        labels = {
            'empid':'Empid','fname' :'Firstname','lname':'Lastname','address':'Address','email':'Email','salary':'Salary','phn_no':'phoneno'
        }

        widgets = {
            'empid': forms.NumberInput(attrs={'class':'form-group'}),
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'salary':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),

            
        }

class customerforms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['fname','lname','address','phn_no','email']
        labels = {
            'fname' :'Firstname','lname':'Lastname','address':'Address','email':'Email','phn_no':'phoneno'
        }

        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'phn_no':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }


class medicineform(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['m_id','mname','dname','desc','price','stock']
        labels = {
            'm_id':'Medid','mname' :'Medicinename','dname':'Dealername','desc':'Description','price':'Price','stock':'Stock'
        }

        widgets = {
            'm_id': forms.NumberInput(attrs={'class':'form-group'}),
            'mname':forms.TextInput(attrs={'class':'form-control'}),
            'dname':forms.TextInput(attrs={'class':'form-control'}),
            'desc':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'stock':forms.NumberInput(attrs={'class':'form-control'}),

            
        }


class purchaseform(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['pname','fname','lname','phn_no','price','qty','total']
        labels = {
            'pname':'Purchase Name','fname' :'First Name','lname':'Last Name','phn_no':'Phone no.','price':'Price','qty':'Quantity','total':'Total'
        }

        widgets = {
            'pname':forms.TextInput(attrs={'class':'form-control'}),
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'phn_no':forms.NumberInput(attrs={'class':'form-control'}),
            'price':forms.NumberInput(attrs={'class':'form-control'}),
            'qty':forms.NumberInput(attrs={'class':'form-control'}),
            'total':forms.NumberInput(attrs={'class':'form-control'}),

            
        }
