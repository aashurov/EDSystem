from django.shortcuts import render, redirect
from customer.forms import *
from userprofile.models import *
from company.models import *
import telegram
from django.conf import settings
from datetime import datetime
from currency.models import *
from customer.models import *


def listmoney(request):
    listmoneys = CustomerAccountHistory.objects.all().select_related('user').order_by('-id')
    loans = CustomerLoan.objects.get(user_id=request.user.id)
    randomm = str(random.randint(1000, 9999))
    return render(request, 'staff/listmoney.html', {"listmoneys": listmoneys, "loans": loans, "random": randomm})


def elistmoney(request, uniq_id, user_id):
    customeraccounthistory = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
    customeraccount = CustomerAccount.objects.get(user_id=user_id)
    if customeraccounthistory.general_status == 'В обработке':
        customeraccounthistory.general_status = 'Одобрено'
        customeraccount.usd = customeraccount.usd + customeraccounthistory.usd
    elif customeraccounthistory.general_status == 'Одобрено':
        customeraccounthistory.general_status = 'В обработке'
        customeraccount.usd = customeraccount.usd - customeraccounthistory.usd
    customeraccount.save()
    customeraccounthistory.save()
    return redirect('stafflistmoney')


def addmoney(request):
    if request.method == 'POST':
        form = CustomerAccountHistoryForm(request.POST)
        customeraccount = CustomerAccount.objects.get(user_id=request.POST['customer_id'])
        if form.is_valid():
            customeraccount.usd = customeraccount.usd + float(request.POST['usd'])
            customeraccount.save()
            obj = form.save(commit=False)
            obj.uniq_id = str(random.randint(1000, 9999))
            obj.general_status = 'Одобрено'
            obj.user_id = request.POST['customer_id']
            obj.courier_id = request.POST['courier_id']
            obj.description = request.POST['description'] + " || " + str(
                request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
            obj.staff_id = request.user.id
            obj.save()
            customername = User.objects.get(pk=request.POST['customer_id'])
            customerbalance = CustomerAccount.objects.get(user_id=request.POST['customer_id'])
            message = "--------Пополнение баланса-------\nКлиент: {} {} {}" \
                      "\nСумма: {}" \
                      "\nБаланс: {}\nКурс: {} || {}\nДата: {}".format(customername.userprofile.uniq_id,
                                                                      customername.last_name,
                                                                      customername.first_name,
                                                                      request.POST['usd'],
                                                                      customerbalance.usd,
                                                                      request.POST['usd_rub'],
                                                                      request.POST['usd_uzs'],
                                                                      datetime.today().strftime('%Y-%m-%d'))
            bot = telegram.Bot(token=settings.BOT_TOKEN)
            bot.sendMessage(chat_id=settings.BOT_CHAT_ID, text=message)
            return redirect('stafflistmoney')
    else:
        form = CustomerAccountHistoryForm()
    currency = CurrencyHistory.objects.all().last()
    customerlist = UserProfile.objects.filter(role='клиент').select_related('user')
    courierlist = UserProfile.objects.filter(role='курер').select_related('user')
    return render(request, 'staff/addmoney.html',
                  {"form": form, "customerlist": customerlist, "courierlist": courierlist, "currency": currency})


def editmoney(request, uniq_id):
    if request.method == 'POST':
        pi = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
        money = CustomerAccountHistoryForm(request.POST, instance=pi)
        if money.is_valid():
            obj = money.save(commit=False)
            obj.staff_id = request.user.id
            obj.description = request.POST['description'] + " || " + str(
                request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
            money.save()
            return redirect('stafflistmoney')
    else:
        pi = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
        money = CustomerAccountHistoryForm(instance=pi)
    description = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
    currency = CurrencyHistory.objects.all().last()
    return render(request, 'staff/editmoney.html', {"money": money, "description": description, "currency": currency})


def deletemoney(request, uniq_id):
    customeraccounthistory = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
    customeraccounthistory.delete()
    return redirect('stafflistmoney')


def customeraccounthistoryview(request, id):
    customeraccounthistoryview = CustomerAccountHistory.objects.get(pk=id)
    customerLFName = User.objects.get(pk=customeraccounthistoryview.user_id)
    courierLFName = User.objects.get(pk=customeraccounthistoryview.courier_id)
    staffLFName = User.objects.get(pk=customeraccounthistoryview.staff_id)
    return render(request, 'staff/modal/customeraccounthistorymodal.html', {
        "customeraccounthistoryview": customeraccounthistoryview,
        "customerLFName": customerLFName,
        "courierLFName": courierLFName,
        "staffLFName": staffLFName})


def customerloanhistoryview(request, id):
    customerloanhistoryview = CustomerLoanHistory.objects.get(pk=id)
    customerLFName = User.objects.get(pk=customerloanhistoryview.user_id)
    staffLFName = User.objects.get(pk=customerloanhistoryview.staff_id)
    return render(request, 'staff/modal/customerloanhistorymodal.html', {
        "customerloanhistoryview": customerloanhistoryview,
        "customerLFName": customerLFName,
        "staffLFName": staffLFName})


def customerexpenseshistoryview(request, id):
    customerexpenseshistoryview = CustomerExpensesHistory.objects.get(pk=id)
    customerLFName = User.objects.get(pk=customerexpenseshistoryview.user_id)
    staffLFName = User.objects.get(pk=customerexpenseshistoryview.staff_id)
    return render(request, 'staff/modal/customerexpenseshistorymodal.html', {
        "customerexpenseshistoryview": customerexpenseshistoryview,
        "customerLFName": customerLFName,
        "staffLFName": staffLFName})


def companyownexpenseshistorysview(request, id):
    companyownexpenseshistorysview = CompanyOwnExpensesHistory.objects.get(pk=id)
    customerLFName = User.objects.get(pk=companyownexpenseshistorysview.user_id)
    staffLFName = User.objects.get(pk=companyownexpenseshistorysview.staff_id)
    return render(request, 'staff/modal/companyownexpenseshistorymodal.html', {
        "companyownexpenseshistorysview": companyownexpenseshistorysview,
        "customerLFName": customerLFName,
        "staffLFName": staffLFName})


def companyexpenseshistorysview(request, id):
    companyexpenseshistorysview = CompanyExpensesHistory.objects.get(pk=id)
    customerLFName = User.objects.get(pk=companyexpenseshistorysview.user_id)
    staffLFName = User.objects.get(pk=companyexpenseshistorysview.staff_id)
    return render(request, 'staff/modal/companyexpenseshistorymodal.html', {
        "companyexpenseshistorysview": companyexpenseshistorysview,
        "customerLFName": customerLFName,
        "staffLFName": staffLFName})


def companyaccounthistorysview(request, id):
    companyaccounthistorysview = CompanyAccountHistory.objects.get(pk=id)
    customerLFName = User.objects.get(pk=companyaccounthistorysview.user_id)
    staffLFName = User.objects.get(pk=companyaccounthistorysview.staff_id)
    return render(request, 'staff/modal/companyaccounthistorymodal.html', {
        "companyaccounthistorysview": companyaccounthistorysview,
        "customerLFName": customerLFName,
        "staffLFName": staffLFName})
