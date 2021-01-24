from django.urls import path
from .staff import *
from .moneymanagement import *
from .loanmanagement import *
from .usermanagement import *
from .companymanagement import *
from .insertuser import *
from .currencymanagement import *
from .customerexpenseshistory import *
from parcel.parcelmanagement import *


urlpatterns = [

    path('', staff, name='staff'),
    path('addmoney', addmoney, name='staffaddmoney'),
    path('listmoney', listmoney, name='stafflistmoney'),
    path('elistmoney/<int:uniq_id>/<int:user_id>', elistmoney, name='elistmoney'),
    path('editmoney/<int:uniq_id>', editmoney, name='staffeditmoney'),
    path('deletemoney/<int:uniq_id>', deletemoney, name='staffdeletemoney'),
    #
    path('listloan', listloan, name='stafflistloan'),
    path('addloan', addloan, name='staffaddloan'),
    path('elistloan/<int:uniq_id>/<int:user_id>/<int:idd>', elistloan, name='elistloan'),
    path('opencloseloan/<int:uniq_id>/<int:user_id>/<int:idd>', opencloseloan, name='opencloseloan'),
    path('editloan/<int:uniq_id>', editloan, name='staffeditloan'),
    path('deleteloan/<int:uniq_id>', deleteloan, name='staffdeleteloan'),
    #
    path('createuser', createuser, name='staffcreateuser'),
    path('listuser', listuser, name='stafflistuser'),
    path('deleteuser/<int:user_id>', deleteuser, name='staffdeleteuser'),
    path('edituser/<int:user_id>', edituser, name='staffediteuser'),
    path('listcourier', listcourier, name='stafflistcourier'),
    path('listcustomermoney', listcustomermoney, name='stafflistcustomermoney'),
    path('listcustomerloan', listcustomerloan, name='stafflistcustomerloan'),
    #
    path('companymoney', companymoney, name='companymoney'),
    path('companymoneysum', companymoneysum, name='companymoneysum'),
    path('companyexpenseshistorys', companyexpenseshistorys, name='companyexpenseshistorys'),
    path('companyownexpenseshistorys', companyownexpenseshistorys, name='companyownexpenseshistorys'),
    path('companyreset', companyreset, name='companyreset'),
    path('getmoneyfromcustomer/<int:user_id>', getmoneyfromcustomer, name='getmoneyfromcustomer'),
    path('deletemoneyfromcustomer/<int:user_id>/<int:uniq_id>', deletemoneyfromcustomer, name='deletemoneyfromcustomer'),
    path('addcompanyownexpenses', addcompanyownexpenses, name='addcompanyownexpenses'),
    path('editcompanyownexpenses/<int:id>', editcompanyownexpenses, name='editcompanyownexpenses'),
    path('deletemoneyfromownexpenses/<int:id>', deletemoneyfromownexpenses, name='deletemoneyfromownexpenses'),
    path('insertuser', insertusero, name='insertuser'),
    path('companycreate', companycreate, name='companycreate'),
    path('counting', counting, name='counting'),
    path('userprofileadd', userprofileadd, name='userprofileadd'),
    path('insertuserphone', insertuserphone, name='insertuserphone'),

    path('listcurrency', listcurency, name='stafflistcurrency'),
    path('addcurrency', addcurrency, name='staffaddcurrency'),
    path('editcurrency/<int:id>', editcurrency, name='staffeditcurrency'),
    path('deletecurrency/<int:id>', deletecurrency, name='staffdeletecurrency'),
    path('listcustomerexpenseshistory', listcustomerexpenseshistory, name='stafflistcustomerexpenseshistory'),
    path('customeraccounthistoryview/<int:id>', customeraccounthistoryview, name='staffcustomeraccounthistoryview'),
    path('customerloanhistoryview/<int:id>', customerloanhistoryview, name='staffcustomerloanhistoryview'),
    path('customerexpenseshistoryview/<int:id>', companyexpenseshistorysview, name='staffcustomerexpenseshistoryview'),
    path('companyownexpenseshistorysview/<int:id>', companyownexpenseshistorysview, name='companyownexpenseshistorysview'),
    path('companyaccounthistorysview/<int:id>', companyaccounthistorysview, name='companyaccounthistorysview'),


    path('listparcel', listparcel, name='listparcel'),
    path('addparcel', addparcel, name='addparcel'),
    path('parcelview/<int:id>', parcelview, name='parcelview'),
    path('deleteparcel/<int:id>', deleteparcel, name='deleteparcel'),
    path('editparcel/<int:id>', editparcel, name='editparcel'),

]
