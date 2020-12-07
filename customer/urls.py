from django.urls import path
from .customer import *
urlpatterns = [
    path('', customer, name='customer'),
    path('listmoney', listmoney, name='customerlistmoney'),
    path('addmoney', addmoney, name='customeraddmoney'),
    path('editmoney/<int:uniq_id>', editmoney, name='customereditmoney'),
    path('deletemoney/<int:uniq_id>', deletemoney, name='customerdeletemoney'),
    #
    path('listloan', listloan, name='customerlistloan'),
    path('addloan', addloan, name='customeraddloan'),
    path('editloan/<int:uniq_id>', editloan, name='customereditloan'),
    path('deleteloan/<int:uniq_id>', deleteloan, name='customerdeleteloan'),
    path('listexpenses', listexpenses, name='customerexpenses'),
    path('customerall', customerall, name='customerall')

]
