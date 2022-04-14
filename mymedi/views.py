from unicodedata import name
from django.shortcuts import redirect, render
from mymedi.models import Dealer
from .models import Customer
from .models import Medicine
from .models import Purchase
from .models import Employee
from .forms import customerforms, dealerform, employeeform, medicineform, purchaseform



# Create your views here.
def indexpage(request):
    return render(request,'index.html')




def dealer(request):
    form = dealerform()
    if request.method == 'POST':
        form = dealerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/dealer")
    
            
    return render(request,"dealer.html",{'forms':form})

def dealertable(request):
    form = dealerform()
    st = Dealer.objects.all()
    return render(request,'dtable.html',{'sm':st})

def dealerupdate(request,id):
    if request.method =='POST':
        pi = Dealer.objects.get(pk=id)
        form = dealerform(request.POST,instance=pi)
        if form.is_valid():
            form.save()
            return redirect('/dtable')
    else:
        pi = Dealer.objects.get(pk=id)
        form = dealerform(instance=pi)        
    return render(request,'dupdate.html',{'fm':form})


def dealerdelete(request,id):
    if request.method == 'POST':
        fi = Dealer.objects.get(pk=id)
        fi.delete()
        return redirect('/dtable')
    


def employee(request):
    efm = employeeform()
    if request.method == 'POST':
        efm = employeeform(request.POST)
        if efm.is_valid():
            efm.save()
            return redirect("/employee")

    return render(request,'employee.html',{'efms':efm})  

def emptable(request):
    efm = employeeform()
    em = Employee.objects.all()
    return render(request,'employeetable.html',{'rm':em})

def empupdate(request,my_id):
    if request.method == 'POST':
        si = Employee.objects.get(pk=my_id)
        empform = employeeform(request.POST,instance=si)
        if empform.is_valid():
            empform.save()
            return redirect("/empupdate/employeetable")
    else:
        si = Employee.objects.get(pk=my_id)
    fi = employeeform(instance=si)
        
    return render(request,'employeeupdate.html',{'sp':fi})

def employeedelete(request,my_id):
    if request.method == 'POST':
        fi = Employee.objects.get(pk=my_id)
        fi.delete()
    return redirect('/empupdate/employeetable/')
                  



def customer(request):
    cfm = customerforms()
    if request.method == 'POST':
        cfm = customerforms(request.POST)
        if cfm.is_valid():
            cfm.save()
            return redirect('/customer')
    return render(request,'customer.html',{'cfms':cfm})

def custtable(request):
    li = customerforms()
    fi = Customer.objects.all()
    return render(request,'customertable.html',{'di':fi})    

def custupdate(request,id):
    if request.method =='POST':
        yv = Customer.objects.get(pk=id)
        yv = customerforms(request.POST,instance=yv)
        if yv.is_valid():
            yv.save()
            return redirect('/customertable')
    else:
        yv = Customer.objects.get(pk=id)
        cd = customerforms(instance=yv)
    return render(request,'customerupdate.html',{'we':cd})
        
def customerdelete(request,id):
    if request.method == 'POST':
        fi = Customer.objects.get(pk=id)
        fi.delete()
        return redirect('/customertable')



def medicine(request):
    mfm = medicineform()
    if request.method =='POST':
        mfm = medicineform(request.POST)
        if mfm.is_valid():
            mfm.save()
            return redirect('/medicine')
    return render(request,'medicine.html',{'md':mfm})                          

def meditable(request):
    ui = medicineform()
    ti = Medicine.objects.all()
    return render(request,'medicinetable.html',{'ri':ti})

def medupdate(request,id):
    if request.method =='POST':
        vy = Medicine.objects.get(pk=id)
        vy = medicineform(request.POST,instance=vy)
        if vy.is_valid():
            vy.save()
            return redirect('/medicinetable')
    else:
        vy = Medicine.objects.get(pk=id)
        dc = medicineform(instance=vy)
    return render(request,'medicineupdate.html',{'ew':dc})  


def medicinedelete(request,id):
    if request.method == 'POST':
        fi = Medicine.objects.get(pk=id)
        fi.delete()
        return redirect('/medicinetable')    

def purchase(request):
    pfm = purchaseform()
    if request.method == 'POST':
        pfm = purchaseform(request.POST)
        if pfm.is_valid():
            pfm.save()
            return redirect('/purchase')
    return render(request,'purchase.html',{'pfms':pfm})        

            
# def purchase(request):
#     if request.method=='POST':
#         price=request.POST.get('price')
#         quantity=request.POST.get('qty')
#         a=price*quantity

#         total=a
#         return render(request,'purchase.html',{'a':a})

def purtable(request):
    ptb = purchaseform()
    ptb = Purchase.objects.all()
    return render(request,'purchasetable.html',{'ptbs':ptb})

def purupdate(request,id):
    if request.method == 'POST':
        pfm = Purchase.objects.get(pk=id)
        pfm = purchaseform(request.POST,instance=pfm)
        if pfm.is_valid():
            pfm.save()
            return redirect('/purchasetable')

    else:
        pfm = Purchase.objects.get(pk=id)
        sy = purchaseform(instance=pfm)
    return render(request,'purupdate.html',{'sys':sy}) 


              
def purchasedelete(request,id):
    if request.method == 'POST':
        fi = Purchase.objects.get(pk=id)
        fi.delete()
        return redirect('/purchasetable')

       
