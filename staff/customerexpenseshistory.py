from django.shortcuts import render
from customer.models import *


def listcustomerexpenseshistory(request):
    customerexpenseshistoryes = CustomerExpensesHistory.objects.all()
    return render(request, 'staff/listcustomerexpenses.html', {"customerexpenseshistoryes": customerexpenseshistoryes})


