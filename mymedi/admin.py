from django.contrib import admin
from .models import Dealer
from .models import Employee
from .models import Customer
from .models import Medicine
from .models import Purchase

# Register your models here.
@admin.register(Dealer)


class dadmin(admin.ModelAdmin):
    list_display = ['dname','address','phone','email']

@admin.register(Employee)


class eadmin(admin.ModelAdmin):
    list_display = ['empid','fname','lname','address','email','salary','phn_no']

@admin.register(Customer)

class cusadmin(admin.ModelAdmin):
    list_display = ['fname','lname','address','phn_no','email']    

@admin.register(Medicine)

class medadmin(admin.ModelAdmin):
    list_display = ['m_id','mname','dname','desc','price','stock']   

@admin.register(Purchase)

class puradmin(admin.ModelAdmin):
    list_display = ['pname','fname','lname','phn_no','price','qty','total']        
