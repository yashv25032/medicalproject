from django.urls import path
from .import views

urlpatterns = [
    path('dealer/',views.dealer,name='dealer'),
    path('',views.indexpage,name='mainpage'),
    path('dtable/',views.dealertable,name='detable'),
    path('update/<int:id>/',views.dealerupdate,name='dupdate'),
    path('delete/<int:id>/',views.dealerdelete,name='delete'),



    path('employee/',views.employee,name='emp'),
    path('empupdate/employeetable/',views.emptable,name='myemp'),
    path('empupdate/<int:my_id>/',views.empupdate,name='empupdate'),
    path('delete/<int:my_id>',views.employeedelete,name='empdel'),



    path('customer/',views.customer,name='cust'),
    path('customertable/',views.custtable,name='custtable'),
    path('custtable/<int:id>',views.custupdate,name='custtable'),
    path('cusdelete/<int:id>',views.customerdelete,name='cusdel'),



    path('medicine/',views.medicine,name='medi'),
    path('medicinetable/',views.meditable,name='meditable'),
    path('medtable/<int:id>',views.medupdate,name='medupdate'),
    path('meddelete/<int:id>',views.medicinedelete,name='meddel'),


    path('purchase/',views.purchase,name='purchase'),
    path('purchasetable/',views.purtable,name='ptable'),
    path('purtable/<int:id>',views.purupdate,name='purupdate'),
    path('purdelete/<int:id>',views.purchasedelete,name='purdel'),





]