from django.shortcuts import render, redirect
from .models import *
from .forms import *
import telegram
from django.conf import settings
from datetime import datetime


# Create your views here.
def customer(request):
    customeraccount = CustomerAccount.objects.get(user_id=request.user.id)
    return render(request, 'customer/dashboard.html', {"customeraccount": customeraccount})


def listmoney(request):
    customeraccounthistorys = CustomerAccountHistory.objects.filter(user_id=request.user.id)
    customeraccount = CustomerAccount.objects.get(user_id=request.user.id)
    return render(request, 'customer/listmoney.html', {
        "customeraccount": customeraccount,
        "customeraccounthistorys": customeraccounthistorys})


def addmoney(request):
    if request.method == 'POST':
        customeraccounthistoryform = CustomerAccountHistoryForm(request.POST)
        if customeraccounthistoryform.is_valid():
            print(request.POST)
            obj = customeraccounthistoryform.save(commit=False)
            obj.user_id = request.user.id
            obj.uniq_id = str(random.randint(1000, 9999))
            obj.save()
            customername = User.objects.get(pk=request.user.id)
            message = "--------Запрос на пополнение-------\nКлиент: {} {}" \
                      "\nВ Долларах: {}\nВ Рублях: {}\nВ Сумах: {}\nВалюты: {}" \
                      "\nДата: {}".format(customername.last_name,
                                          customername.first_name,
                                          request.POST['usd'],
                                          request.POST['rub'],
                                          request.POST['uzs'],
                                          request.POST['currency_type'],
                                          datetime.today().strftime('%Y-%m-%d'))
            bot = telegram.Bot(token=settings.BOT_TOKEN)
            bot.sendMessage(chat_id=settings.BOT_CHAT_ID, text=message)
            return redirect('customerlistmoney')
    else:
        customeraccounthistoryform = CustomerAccountHistoryForm()
    return render(request, 'customer/addmoney.html', {"customeraccounthistoryform": customeraccounthistoryform})


def editmoney(request, uniq_id):
    if request.method == 'POST':
        customeraccounthistory = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
        customeraccounthistoryform = CustomerAccountHistoryForm(request.POST, instance=customeraccounthistory)
        if customeraccounthistoryform.is_valid():
            customeraccounthistoryform.save()
            return redirect('customerlistmoney')
    else:
        customeraccounthistory = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
        customeraccounthistoryform = CustomerAccountHistoryForm(instance=customeraccounthistory)
    customeraccount = CustomerAccount.objects.get(user_id=request.user.id)
    return render(request, 'customer/editmoney.html',
                  {"customeraccounthistoryform": customeraccounthistoryform,
                   "customeraccount": customeraccount})


def deletemoney(request, uniq_id):
    customeraccounthistory = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
    customeraccounthistory.delete()
    return redirect('customerlistmoney')


def listloan(request):
    customerloanhistorys = CustomerLoanHistory.objects.filter(user_id=request.user.id)
    customeraccount = CustomerAccount.objects.get(user_id=request.user.id)
    return render(request, 'customer/listloan.html',
                  {"customerloanhistorys": customerloanhistorys, "customeraccount": customeraccount})


def addloan(request):
    if request.method == 'POST':
        customerloanform = CustomerLoanForm(request.POST)
        if customerloanform.is_valid():
            obj = customerloanform.save(commit=False)
            obj.user_id = request.user.id
            obj.uniq_id = str(random.randint(1000, 9999))
            obj.save()
            return redirect('customerlistloan')
    else:
        customerloanform = CustomerLoanForm()
    customeraccount = CustomerAccount.objects.get(user_id=request.user.id)
    return render(request, 'customer/addloan.html',
                  {"customerloanform": customerloanform, "customeraccount": customeraccount})


def editloan(request, uniq_id):
    if request.method == 'POST':
        pi = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
        customerloanhistoryform = CustomerLoanHistoryForm(request.POST, instance=pi)
        if customerloanhistoryform.is_valid():
            customerloanhistoryform.save()
            return redirect('customerlistloan')
    else:
        pi = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
        customerloanhistoryform = CustomerLoanHistoryForm(instance=pi)
    customeraccount = CustomerAccount.objects.get(user_id=request.user.id)
    return render(request, 'customer/editloan.html',
                  {"customerloanhistoryform": customerloanhistoryform, "customeraccount": customeraccount})


def deleteloan(request, uniq_id):
    loan = CustomerLoanHistory.objects.get(uniq_id=uniq_id)
    loan.delete()
    return redirect('customerlistloan')


def listexpenses(request):
    customerexpenseshistorys = CustomerExpensesHistory.objects.filter(user_id=request.user.id)
    customeraccount = CustomerAccount.objects.get(user_id=request.user.id)
    return render(request, 'customer/listexpenses.html',
                  {"customerexpenseshistorys": customerexpenseshistorys, "customeraccount": customeraccount})


def customerall(request):
    customeraccount = CustomerAccount.objects.get(user_id=request.user.id)
    customerloan = CustomerLoan.objects.get(user_id=request.user.id)
    customerexpenses = CustomerExpenses.objects.get(user_id=request.user.id)
    return render(request, 'customer/customermoneysum.html',
                  {"customeraccount": customeraccount, "customerloan": customerloan,
                   "customerexpenses": customerexpenses})
