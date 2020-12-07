from django.shortcuts import render, redirect
from customer.models import *
from company.forms import *
from django.db import connection
from main.models import *
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm
from userprofile.forms import ProfileUpdateForm, UserUpdateForm
from company.models import *
from currency.models import *


def companycreate(request):
    companyexpenses = CompanyExpenses()
    companyexpenses.usd = 0
    companyexpenses.rub = 0
    companyexpenses.uzs = 0
    companyexpenses.save()
    companyaccount = CompanyAccount()
    companyaccount.usd = 10000
    companyaccount.rub = 7700
    companyaccount.uzs = 1050000
    companyaccount.save()
    return redirect('staff')


def companyreset(request):
    companyaccount = CompanyAccount.objects.get(pk=1)
    companyaccount.usd = 10000
    companyaccount.rub = 7700
    companyaccount.uzs = 1050000
    companyaccount.save()
    CustomerLoanHistory.objects.all().delete()
    CustomerAccountHistory.objects.all().delete()
    CustomerExpensesHistory.objects.all().delete()
    CompanyAccountHistory.objects.all().delete()
    companyexpenses = CompanyExpenses.objects.all()
    for x in companyexpenses:
        x.usd = 0
        x.rub = 0
        x.uzs = 0
        x.save()
    customerexpenses = CustomerExpenses.objects.all()
    for x in customerexpenses:
        x.usd = 0
        x.rub = 0
        x.uzs = 0
        x.save()
    customeraccount = CustomerAccount.objects.all()
    for x in customeraccount:
        x.usd = 0
        x.rub = 0
        x.uzs = 0
        x.save()
    customerloan = CustomerLoan.objects.all()
    for x in customerloan:
        x.usd = 0
        x.rub = 0
        x.uzs = 0
        x.save()
    user = User.objects.all()
    return redirect('staff')


def companymoney(request):
    companymoneys = CompanyAccountHistory.objects.all().order_by('-id')
    return render(request, 'staff/companymoney.html', {"companymoneys": companymoneys})


def companymoneysum(request):
    companyaccount = CompanyAccount.objects.get(pk=1)
    companyexpenses = CompanyExpenses.objects.get(pk=1)
    return render(request, 'staff/companymoneysum.html', {"companyaccount": companyaccount, "companyexpenses": companyexpenses })


def companyexpenseshistorys(request):
    companyexpenseshistorys = CompanyExpensesHistory.objects.all().order_by('-id')
    return render(request, 'staff/companyexpenses.html', {"companyexpenseshistorys": companyexpenseshistorys})


def getmoneyfromcustomer(request, user_id):
    if request.method == 'POST':
        customeraccount = CustomerAccount.objects.get(pk=user_id)
        form = CompanyAccountHistoryForm(request.POST)
        if form.is_valid():
            if request.POST['service_type'] == 'За Товар':
                obj = form.save(commit=False)
                obj.user_id = user_id
                general_uniq_id = str(random.randint(1000, 9999))
                obj.uniq_id = general_uniq_id
                obj.usd = float(request.POST['usd']) / 100
                obj.rub = float(request.POST['rub']) / 100
                obj.uzs = float(request.POST['uzs']) / 100
                obj.plan_type = '00'
                obj.save()
                companyaccaount = CompanyAccount.objects.get(pk=1)
                companyaccaount.usd = companyaccaount.usd + float(request.POST['usd']) / 100
                companyaccaount.rub = companyaccaount.rub + float(request.POST['rub']) / 100
                companyaccaount.uzs = companyaccaount.uzs + float(request.POST['uzs']) / 100
                companyaccaount.save()
                customeraccount.usd = customeraccount.usd - float(request.POST['usd']) - float(request.POST['usd']) / 100
                customeraccount.rub = customeraccount.rub - float(request.POST['rub']) - float(request.POST['rub']) / 100
                customeraccount.uzs = customeraccount.uzs - float(request.POST['uzs']) - float(request.POST['uzs']) / 100
                customeraccount.save()
                customerexpenseshistory = CustomerExpensesHistory()
                customerexpenseshistory.user_id = user_id
                customerexpenseshistory.usd = float(request.POST['usd']) + float(request.POST['usd']) / 100
                customerexpenseshistory.rub = float(request.POST['rub']) + float(request.POST['rub']) / 100
                customerexpenseshistory.uzs = float(request.POST['uzs']) + float(request.POST['uzs']) / 100
                customerexpenseshistory.plan_type = '00'
                customerexpenseshistory.service_type = request.POST['service_type']
                customerexpenseshistory.currency_type = request.POST['currency_type']
                customerexpenseshistory.save()
                customerexpenses = CustomerExpenses.objects.get(user_id=user_id)
                customerexpenses.usd = float(request.POST['usd']) + float(request.POST['usd']) / 100
                customerexpenses.rub = float(request.POST['rub']) + float(request.POST['rub']) / 100
                customerexpenses.uzs = float(request.POST['uzs']) + float(request.POST['uzs']) / 100
                customerexpenses.save()
            else:
                obj = form.save(commit=False)
                obj.user_id = user_id
                general_uniq_id = str(random.randint(1000, 9999))
                obj.uniq_id = general_uniq_id
                obj.usd = float(request.POST['usd'])
                obj.rub = float(request.POST['rub'])
                obj.uzs = float(request.POST['uzs'])
                obj.save()
                companyaccaount = CompanyAccount.objects.get(pk=1)
                companyaccaount.usd = companyaccaount.usd + float(request.POST['usd'])
                companyaccaount.rub = companyaccaount.rub + float(request.POST['rub'])
                companyaccaount.uzs = companyaccaount.uzs + float(request.POST['uzs'])
                companyaccaount.save()
                customeraccount.usd = customeraccount.usd - float(request.POST['usd'])
                customeraccount.rub = customeraccount.rub - float(request.POST['rub'])
                customeraccount.uzs = customeraccount.uzs - float(request.POST['uzs'])
                customeraccount.save()
                customerexpenseshistory = CustomerExpensesHistory()
                customerexpenseshistory.user_id = user_id
                customerexpenseshistory.uniq_id = general_uniq_id
                customerexpenseshistory.usd = float(request.POST['usd'])
                customerexpenseshistory.rub = float(request.POST['rub'])
                customerexpenseshistory.uzs = float(request.POST['uzs'])
                customerexpenseshistory.plan_type = request.POST['plan_type']
                customerexpenseshistory.service_type = request.POST['service_type']
                customerexpenseshistory.currency_type = request.POST['currency_type']
                customerexpenseshistory.save()
                customerexpenses = CustomerExpenses.objects.get(user_id=user_id)
                customerexpenses.usd = float(request.POST['usd'])
                customerexpenses.rub = float(request.POST['rub'])
                customerexpenses.uzs = float(request.POST['uzs'])
                customerexpenses.save()
            return redirect('stafflistcustomermoney')
    else:
        pi = CustomerAccount.objects.get(pk=user_id)
        form = CompanyAccountHistoryForm()
    currency = CurrencyHistory.objects.all().last()
    return render(request, 'staff/addmoneyy.html', {"form": form, "pi":pi, "currency":currency})


def deletemoneyfromcustomer(request, user_id, uniq_id):
    companyaccounthistory = CompanyAccountHistory.objects.get(uniq_id=uniq_id)
    companyaccount = CompanyAccount.objects.get(pk=1)
    if companyaccounthistory.service_type == 'За Товар':
        companyaccounthistory.usd = companyaccounthistory.usd * 100 + companyaccounthistory.usd
        companyaccounthistory.rub = companyaccounthistory.rub * 100 + companyaccounthistory.rub
        companyaccounthistory.uzs = companyaccounthistory.uzs * 100 + companyaccounthistory.uzs
        companyaccount = CompanyAccount.objects.get(pk=1)
        companyaccount.usd = companyaccount.usd - companyaccounthistory.usd
        companyaccount.rub = companyaccount.rub - companyaccounthistory.rub
        companyaccount.uzs = companyaccount.uzs - companyaccounthistory.uzs
        companyaccount.save()
        customerexpenses = CustomerExpenses.objects.get(user_id=user_id)
        customerexpenses.usd = customerexpenses.usd - companyaccounthistory.usd
        customerexpenses.rub = customerexpenses.rub - companyaccounthistory.rub
        customerexpenses.uzs = customerexpenses.uzs - companyaccounthistory.uzs
        customerexpenses.save()
        customeraccount = CustomerAccount.objects.get(user_id=user_id)
        customeraccount.usd = customeraccount.usd + companyaccounthistory.usd
        customeraccount.rub = customeraccount.rub + companyaccounthistory.rub
        customeraccount.uzs = customeraccount.uzs + companyaccounthistory.uzs
        customeraccount.save()
        customerexpenseshistory = CustomerExpensesHistory.objects.get(user_id=user_id)
        customerexpenseshistory.delete()
        companyaccounthistory.delete()
    else:
        companyaccount.usd = companyaccount.usd - companyaccounthistory.usd
        companyaccount.rub = companyaccount.rub - companyaccounthistory.rub
        companyaccount.uzs = companyaccount.uzs - companyaccounthistory.uzs
        companyaccount.save()
        customerexpenses = CustomerExpenses.objects.get(user_id=user_id)
        customerexpenses.usd = customerexpenses.usd - companyaccounthistory.usd
        customerexpenses.rub = customerexpenses.rub - companyaccounthistory.rub
        customerexpenses.uzs = customerexpenses.uzs - companyaccounthistory.uzs
        customerexpenses.save()
        customeraccount = CustomerAccount.objects.get(user_id=user_id)
        customeraccount.usd = customeraccount.usd + companyaccounthistory.usd
        customeraccount.rub = customeraccount.rub + companyaccounthistory.rub
        customeraccount.uzs = customeraccount.uzs + companyaccounthistory.uzs
        customeraccount.save()
        customerexpenseshistory = CustomerExpensesHistory.objects.get(user_id=user_id)
        customerexpenseshistory.delete()
        companyaccounthistory.delete()
    return redirect('companymoney')
