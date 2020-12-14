from django.shortcuts import render, redirect
from customer.forms import *
from userprofile.models import *
from company.models import *
from currency.models import *


def listloan(request):
    loans = CustomerLoanHistory.objects.all().order_by('-id')
    return render(request, 'staff/listloan.html', {"loans": loans})


def addloan(request):
    if request.method == 'POST':
        form = CustomerLoanHistoryForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.uniq_id = str(random.randint(1000, 9999))
            obj.user_id = request.POST['user_id']
            obj.staff_id = request.user.id
            obj.description = request.POST['description'] + " || " + str(request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
            obj.general_status = 'Одобрено'
            obj.loan_status = 'Взял'
            obj.save()
            customerloan = CustomerLoan.objects.get(user_id=request.POST['user_id'])
            customerloan.usd = customerloan.usd + float(request.POST['usd'])
            customerloan.save()
            companyexpenseshistory = CompanyExpensesHistory()
            companyexpenseshistory.user_id = request.POST['user_id']
            companyexpenseshistory.uniq_id = str(random.randint(1000, 9999))
            companyexpenseshistory.customer_loan_history = CustomerLoanHistory.objects.latest('id')
            companyexpenseshistory.company_expenses_type = 'За Долги'
            companyexpenseshistory.usd = float(request.POST['usd'])
            companyexpenseshistory.save()
            companyexpenses = CompanyExpenses.objects.get(pk=1)
            companyexpenses.usd = companyexpenses.usd + float(request.POST['usd'])
            companyexpenses.save()
            companyaccount = CompanyAccount.objects.get(pk=1)
            companyaccount.usd = companyaccount.usd - float(request.POST['usd'])
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
        companyexpenseshistory = CompanyExpensesHistory()
        companyexpenseshistory.user_id = customerloanhistory.user_id
        companyexpenseshistory.uniq_id = str(random.randint(1000, 9999))
        companyexpenseshistory.customer_loan_history = CustomerLoanHistory.objects.latest('id')
        companyexpenseshistory.company_expenses_type = 'За Долги'
        companyexpenseshistory.usd = customerloanhistory.usd
        companyexpenseshistory.save()
        companyexpenses = CompanyExpenses.objects.get(pk=1)
        companyexpenses.usd = companyexpenses.usd + customerloanhistory.usd
        companyexpenses.save()
        companyaccount = CompanyAccount.objects.get(pk=1)
        companyaccount.usd = companyaccount.usd - customerloanhistory.usd
        companyaccount.save()
    elif customerloanhistory.general_status == 'Одобрено':
        customerloanhistory.general_status = 'В обработке'
        customerloan.usd = customerloan.usd - customerloanhistory.usd
        companyaccount = CompanyAccount.objects.get(pk=1)
        companyaccount.usd = companyaccount.usd + customerloanhistory.usd
        companyaccount.save()
        companyexpenses = CompanyExpenses.objects.get(pk=1)
        companyexpenses.usd = companyexpenses.usd - customerloanhistory.usd
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
        companyaccount.usd = companyaccount.usd + customerloanhistory.usd
        companyexpenses.usd = companyexpenses.usd - customerloanhistory.usd
        companyaccounthistory = CompanyAccountHistory()
        companyaccounthistory.uniq_id = uniq_id
        companyaccounthistory.service_type = 'За долги'
        companyaccounthistory.plan_type = '00'
        companyaccounthistory.user_id = user_id
        companyaccounthistory.usd = customerloanhistory.usd
        companyaccounthistory.save()
        companyexpenses.save()
        companyaccount.save()
        customerloan.save()
        customerloanhistory.save()
    elif customerloanhistory.loan_status == 'Вернул':
        customerloanhistory.loan_status = 'Взял'
        customerloan.usd = customerloan.usd + customerloanhistory.usd
        companyaccount.usd = companyaccount.usd - customerloanhistory.usd
        companyexpenses.usd = companyexpenses.usd + customerloanhistory.usd
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
            obj = loan.save(commit=False)
            obj.staff_id = request.user.id
            obj.description = request.POST['description'] + " || " + str(request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
            loan.save()
            return redirect('stafflistloan')
    else:
        pi = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
        loan = CustomerAccountForm(instance=pi)
    currency = CurrencyHistory.objects.all().last()
    description = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
    return render(request, 'staff/editloan.html', {"loan": loan, "currency": currency, "description": description})


def deleteloan(request, uniq_id):
    loan = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
    loan.delete()
    return redirect('stafflistloan')