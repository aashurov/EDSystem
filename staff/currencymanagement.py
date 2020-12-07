from django.shortcuts import render, redirect
from customer.models import *
from customer.forms import *
from django.db import connection
from main.models import *
from userprofile.models import *
from company.models import *
from currency.models import *
from currency.forms import *


def listcurency(request):
    currencyhistories = CurrencyHistory.objects.all()
    return render(request, 'currency/listcurrency.html', {"currencyhistories": currencyhistories})


def addcurrency(request):
    if request.method == 'POST':
        currencyhistoryform = CurrencyHistoryForm(request.POST)
        if currencyhistoryform.is_valid():
            currencyhistoryform.save()
            return redirect('stafflistcurrency')
    else:
        currencyhistoryform = CurrencyHistoryForm()
    return render(request, 'currency/addcurrency.html', {"currencyhistoryform": currencyhistoryform})


def editcurrency(request, id):
    if request.method == 'POST':
        pi = CurrencyHistory.objects.get(id=id)
        currencyhistoryform = CurrencyHistoryForm(request.POST, instance=pi)
        if currencyhistoryform.is_valid():
            currencyhistoryform.save()
            return redirect('stafflistcurrency')
    else:
        pi = CurrencyHistory.objects.get(id=id)
        currencyhistoryform = CurrencyHistoryForm(instance=pi)
    return render(request, 'currency/editcurrency.html', {"currencyhistoryform": currencyhistoryform})


def deletecurrency(request, id):
    currency = CurrencyHistory.objects.get(id=id)
    currency.delete()
    return redirect('stafflistcurrency')