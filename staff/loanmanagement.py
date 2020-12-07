from django.shortcuts import render, redirect
from customer.models import *
from customer.forms import *
from django.db import connection
from main.models import *
from userprofile.models import *
from company.models import *
from currency.models import *


def listloan(request):
    loans = CustomerLoanHistory.objects.all()
    return render(request, 'staff/listloan.html', {"loans": loans})


def addloan(request):
    print("Salom")
    if request.method == 'POST':
        form = CustomerLoanHistoryForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.uniq_id = str(random.randint(1000, 9999))
            obj.user_id = request.POST['user_id']
            obj.general_status = 'Одобрено'
            obj.loan_status = 'Взял'
            obj.save()
            customerloan = CustomerLoan.objects.get(user_id=request.POST['user_id'])
            customerloan.usd = customerloan.usd + float(request.POST['usd'])
            customerloan.rub = customerloan.rub + float(request.POST['rub'])
            customerloan.uzs = customerloan.uzs + float(request.POST['uzs'])
            customerloan.save()
            companyexpenseshistory = CompanyExpensesHistory()
            companyexpenseshistory.user_id = request.POST['user_id']
            companyexpenseshistory.uniq_id = str(random.randint(1000, 9999))
            companyexpenseshistory.customer_loan_history = CustomerLoanHistory.objects.latest('id')
            companyexpenseshistory.currency_type = request.POST['currency_type']
            companyexpenseshistory.company_expenses_type = 'За Долги'
            companyexpenseshistory.usd = float(request.POST['usd'])
            companyexpenseshistory.rub = float(request.POST['rub'])
            companyexpenseshistory.uzs = float(request.POST['uzs'])
            companyexpenseshistory.save()
            companyexpenses = CompanyExpenses.objects.get(pk=1)
            companyexpenses.usd = companyexpenses.usd + float(request.POST['usd'])
            companyexpenses.rub = companyexpenses.rub + float(request.POST['rub'])
            companyexpenses.uzs = companyexpenses.uzs + float(request.POST['uzs'])
            companyexpenses.save()
            companyaccount = CompanyAccount.objects.get(pk=1)
            companyaccount.usd = companyaccount.usd - float(request.POST['usd'])
            companyaccount.rub = companyaccount.rub - float(request.POST['rub'])
            companyaccount.uzs = companyaccount.uzs - float(request.POST['uzs'])
            companyaccount.save()
            return redirect('stafflistloan')
    else:
        form = CustomerLoanForm()
    objectlist = UserProfile.objects.filter(role='клиент').select_related('user')
    currency = CurrencyHistory.objects.all().last()
    userloansum = CustomerLoan.objects.get(user_id=request.user.id)
    return render(request, 'staff/addloan.html', {"form": form, "sum": userloansum, "objectlist": objectlist, "currency":currency})


def elistloan(request, uniq_id, user_id, idd):
    customerloanhistory = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
    customerloan = CustomerLoan.objects.get(pk=user_id)
    if customerloanhistory.general_status == 'В обработке':
        customerloanhistory.general_status = 'Одобрено'
        customerloan.usd = customerloan.usd + customerloanhistory.usd
        customerloan.rub = customerloan.rub + customerloanhistory.rub
        customerloan.uzs = customerloan.uzs + customerloanhistory.uzs
        companyexpenseshistory = CompanyExpensesHistory()
        companyexpenseshistory.user_id = customerloanhistory.user_id
        companyexpenseshistory.uniq_id = str(random.randint(1000, 9999))
        companyexpenseshistory.customer_loan_history = CustomerLoanHistory.objects.latest('id')
        companyexpenseshistory.currency_type = customerloanhistory.currency_type
        companyexpenseshistory.company_expenses_type = 'За Долги'
        companyexpenseshistory.usd = customerloanhistory.usd
        companyexpenseshistory.rub = customerloanhistory.rub
        companyexpenseshistory.uzs = customerloanhistory.uzs
        companyexpenseshistory.save()
        companyexpenses = CompanyExpenses.objects.get(pk=1)
        companyexpenses.usd = companyexpenses.usd + customerloanhistory.usd
        companyexpenses.rub = companyexpenses.rub + customerloanhistory.rub
        companyexpenses.uzs = companyexpenses.uzs + customerloanhistory.uzs
        companyexpenses.save()
        companyaccount = CompanyAccount.objects.get(pk=1)
        companyaccount.usd = companyaccount.usd - customerloanhistory.usd
        companyaccount.rub = companyaccount.rub - customerloanhistory.rub
        companyaccount.uzs = companyaccount.uzs - customerloanhistory.uzs
        companyaccount.save()
    elif customerloanhistory.general_status == 'Одобрено':
        customerloanhistory.general_status = 'В обработке'
        customerloan.usd = customerloan.usd - customerloanhistory.usd
        customerloan.rub = customerloan.rub - customerloanhistory.rub
        customerloan.uzs = customerloan.uzs - customerloanhistory.uzs
        companyaccount = CompanyAccount.objects.get(pk=1)
        companyaccount.usd = companyaccount.usd + customerloanhistory.usd
        companyaccount.rub = companyaccount.rub + customerloanhistory.rub
        companyaccount.uzs = companyaccount.uzs + customerloanhistory.uzs
        companyaccount.save()
        companyexpenses = CompanyExpenses.objects.get(pk=1)
        companyexpenses.usd = companyexpenses.usd - customerloanhistory.usd
        companyexpenses.rub = companyexpenses.rub - customerloanhistory.rub
        companyexpenses.uzs = companyexpenses.uzs - customerloanhistory.uzs
        companyexpenses.save()
        companyexpenseshistory = CompanyExpensesHistory.objects.get(customer_loan_history_id=idd)
        companyexpenseshistory.delete()
    customerloan.save()
    customerloanhistory.save()
    return redirect('stafflistloan')


def opencloseloan(request, uniq_id, user_id, idd):
    customerloanhistory = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
    customerloan = CustomerLoan.objects.get(user_id=user_id)
    companyaccount = CompanyAccount.objects.get(pk=1)
    companyexpenses = CompanyExpenses.objects.get(pk=1)
    if customerloanhistory.loan_status == 'Взял':
        customerloanhistory.loan_status = 'Вернул'
        customerloan.usd = customerloan.usd - customerloanhistory.usd
        customerloan.rub = customerloan.rub - customerloanhistory.rub
        customerloan.uzs = customerloan.uzs - customerloanhistory.uzs
        companyaccount.usd = companyaccount.usd + customerloanhistory.usd
        companyaccount.rub = companyaccount.rub + customerloanhistory.rub
        companyaccount.uzs = companyaccount.uzs + customerloanhistory.uzs
        companyexpenses.usd = companyexpenses.usd - customerloanhistory.usd
        companyexpenses.rub = companyexpenses.rub - customerloanhistory.rub
        companyexpenses.uzs = companyexpenses.uzs - customerloanhistory.uzs
        companyaccounthistory = CompanyAccountHistory()
        companyaccounthistory.uniq_id = uniq_id
        companyaccounthistory.service_type = 'За долги'
        companyaccounthistory.currency_type = customerloanhistory.currency_type
        companyaccounthistory.plan_type = '00'
        companyaccounthistory.user_id = user_id
        companyaccounthistory.usd = customerloanhistory.usd
        companyaccounthistory.rub = customerloanhistory.rub
        companyaccounthistory.uzs = customerloanhistory.uzs
        companyaccounthistory.save()
        companyexpenses.save()
        companyaccount.save()
        customerloan.save()
        customerloanhistory.save()
    elif customerloanhistory.loan_status == 'Вернул':
        print("sa")
        customerloanhistory.loan_status = 'Взял'
        customerloan.usd = customerloan.usd + customerloanhistory.usd
        customerloan.rub = customerloan.rub + customerloanhistory.rub
        customerloan.uzs = customerloan.uzs + customerloanhistory.uzs
        companyaccount.usd = companyaccount.usd - customerloanhistory.usd
        companyaccount.rub = companyaccount.rub - customerloanhistory.rub
        companyaccount.uzs = companyaccount.uzs - customerloanhistory.uzs
        companyexpenses.usd = companyexpenses.usd + customerloanhistory.usd
        companyexpenses.rub = companyexpenses.rub + customerloanhistory.rub
        companyexpenses.uzs = companyexpenses.uzs + customerloanhistory.uzs
        companyaccounthistory = CompanyAccountHistory.objects.get(uniq_id=uniq_id)
        companyaccounthistory.delete()
        customerloanhistory.save()
        customerloan.save()
        companyaccount.save()
        companyexpenses.save()
    return redirect('stafflistloan')


def editloan(request, uniq_id):
    if request.method == 'POST':
        pi = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
        loan = CustomerAccountForm(request.POST, instance=pi)
        if loan.is_valid():
            loan.save()
            return redirect('stafflistloan')
    else:
        pi = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
        loan = CustomerAccountForm(instance=pi)
    currency = CurrencyHistory.objects.all().last()
    return render(request, 'staff/editloan.html', {"loan": loan, "currency":currency})


def deleteloan(request, uniq_id):
    loan = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
    loan.delete()
    return redirect('stafflistloan')