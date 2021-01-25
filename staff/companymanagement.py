from django.shortcuts import render, redirect
from company.forms import *
from company.models import *
from currency.models import *
from userprofile.models import *
import telegram
from django.conf import settings
from datetime import datetime


def companycreate(request):
    companyexpenses = CompanyExpenses()
    companyexpenses.usd = 0
    companyexpenses.save()
    companyaccount = CompanyAccount()
    companyaccount.usd = 0
    companyaccount.save()
    return redirect('staff')


def companyreset(request):
    companyaccount = CompanyAccount.objects.get(pk=1)
    companyaccount.usd = 10000
    companyaccount.save()
    CustomerLoanHistory.objects.all().delete()
    CustomerAccountHistory.objects.all().delete()
    CustomerExpensesHistory.objects.all().delete()
    CompanyOwnExpensesHistory.objects.all().delete()
    CompanyAccountHistory.objects.all().delete()
    companyexpenses = CompanyExpenses.objects.all()
    for x in companyexpenses:
        x.usd = 0
        x.save()
    customerexpenses = CustomerExpenses.objects.all()
    for x in customerexpenses:
        x.usd = 0
        x.save()
    customeraccount = CustomerAccount.objects.all()
    for x in customeraccount:
        x.usd = 0
        x.save()
    customerloan = CustomerLoan.objects.all()
    for x in customerloan:
        x.usd = 0
        x.save()
    return redirect('staff')


def companymoney(request):
    companymoneys = CompanyAccountHistory.objects.all().order_by('-id')
    return render(request, 'staff/companymoney.html', {"companymoneys": companymoneys})


def companymoneysum(request):
    companyaccount = CompanyAccount.objects.get(pk=1)
    companyexpenses = CompanyExpenses.objects.get(pk=1)
    return render(request, 'staff/companymoneysum.html',
                  {"companyaccount": companyaccount, "companyexpenses": companyexpenses})


def companyexpenseshistorys(request):
    companyexpenseshistorys = CompanyExpensesHistory.objects.all().order_by('-id')
    return render(request, 'staff/companyexpenses.html', {"companyexpenseshistorys": companyexpenseshistorys})


def companyownexpenseshistorys(request):
    companyownexpenseshistorys = CompanyOwnExpensesHistory.objects.all().order_by('-id')
    return render(request, 'staff/companyownexpenses.html', {"companyownexpenseshistorys": companyownexpenseshistorys})


def getmoneyfromcustomer(request, user_id):
    if request.method == 'POST':
        customeraccount = CustomerAccount.objects.get(pk=user_id)
        form = CompanyAccountHistoryForm(request.POST)
        if form.is_valid():
            if request.POST['service_type'] == 'Вернуть клиенту':
                customeraccount.usd = customeraccount.usd - float(request.POST['usd'])
                customeraccount.save()
                general_uniq_id = str(random.randint(1000, 9999))
                customerexpenseshistory = CustomerExpensesHistory()
                customerexpenseshistory.user_id = user_id
                customerexpenseshistory.uniq_id = general_uniq_id
                customerexpenseshistory.usd = float(request.POST['usd'])
                customerexpenseshistory.plan_type = '00'
                customerexpenseshistory.service_type = request.POST['service_type']
                customerexpenseshistory.staff_id = request.user.id
                customerexpenseshistory.description = request.POST['description'] + " || " + str(
                    request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
                customerexpenseshistory.save()
                customerexpenses = CustomerExpenses.objects.get(user_id=user_id)
                customerexpenses.usd = customerexpenses.usd + float(request.POST['usd'])
                customerexpenses.save()
            elif request.POST['service_type'] == 'За Товар':
                if customeraccount.usd>float(request.POST['usd']) or customeraccount.usd!=float(request.POST['usd']):
                    obj = form.save(commit=False)
                    obj.user_id = user_id
                    general_uniq_id = str(random.randint(1000, 9999))
                    obj.uniq_id = general_uniq_id
                    obj.usd = float(request.POST['usd']) / 100
                    obj.plan_type = '00'
                    obj.staff_id = request.user.id
                    obj.description = request.POST['description'] + " || " + str(request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
                    obj.save()
                    companyaccaount = CompanyAccount.objects.get(pk=1)
                    companyaccaount.usd = companyaccaount.usd + float(request.POST['usd']) / 100
                    companyaccaount.save()
                    customeraccount.usd = customeraccount.usd - float(request.POST['usd']) - float(request.POST['usd']) / 100
                    customeraccount.save()
            else:
                obj = form.save(commit=False)
                obj.user_id = user_id
                general_uniq_id = str(random.randint(1000, 9999))
                obj.uniq_id = general_uniq_id
                obj.usd = float(request.POST['usd'])
                obj.staff_id = request.user.id
                obj.description = request.POST['description'] + " || " + str(request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
                obj.save()
                companyaccaount = CompanyAccount.objects.get(pk=1)
                companyaccaount.usd = companyaccaount.usd + float(request.POST['usd'])
                companyaccaount.save()
                customeraccount.usd = customeraccount.usd - float(request.POST['usd'])
                customeraccount.save()
                customerexpenseshistory = CustomerExpensesHistory()
                customerexpenseshistory.user_id = user_id
                customerexpenseshistory.uniq_id = general_uniq_id
                customerexpenseshistory.usd = float(request.POST['usd'])
                customerexpenseshistory.plan_type = request.POST['plan_type']
                customerexpenseshistory.service_type = request.POST['service_type']
                customerexpenseshistory.staff_id = request.user.id
                customerexpenseshistory.description = request.POST['description'] + " || " + str(
                request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
                customerexpenseshistory.save()
                customerexpenses = CustomerExpenses.objects.get(user_id=user_id)
                customerexpenses.usd = customerexpenses.usd + float(request.POST['usd'])
                customerexpenses.save()
            return redirect('stafflistcustomermoney')
    else:
        pi = CustomerAccount.objects.get(pk=user_id)
        form = CompanyAccountHistoryForm()
    currency = CurrencyHistory.objects.all().last()
    return render(request, 'staff/addmoneyy.html', {"form": form, "pi": pi, "currency": currency})


def deletemoneyfromcustomer(request, user_id, uniq_id):
    companyaccounthistory = CompanyAccountHistory.objects.get(uniq_id=uniq_id)
    companyaccount = CompanyAccount.objects.get(pk=1)
    if companyaccounthistory.service_type == 'За Товар':
        # companyaccounthistory.usd = companyaccounthistory.usd * 100 + companyaccounthistory.usd
        companyaccount = CompanyAccount.objects.get(pk=1)
        companyaccount.usd = companyaccount.usd - companyaccounthistory.usd
        companyaccount.save()
        customerexpenses = CustomerExpenses.objects.get(user_id=user_id)
        customerexpenses.usd = customerexpenses.usd - companyaccounthistory.usd
        customerexpenses.save()
        customeraccount = CustomerAccount.objects.get(user_id=user_id)
        companyaccounthistory.usd = companyaccounthistory.usd * 100 + companyaccounthistory.usd
        customeraccount.usd = customeraccount.usd + companyaccounthistory.usd
        customeraccount.save()
        customerexpenseshistory = CustomerExpensesHistory.objects.get(uniq_id=uniq_id)
        customerexpenseshistory.delete()
        companyaccounthistory.delete()
    else:
        companyaccount.usd = companyaccount.usd - companyaccounthistory.usd
        companyaccount.save()
        customerexpenses = CustomerExpenses.objects.get(user_id=user_id)
        customerexpenses.usd = customerexpenses.usd - companyaccounthistory.usd
        customerexpenses.save()
        customeraccount = CustomerAccount.objects.get(user_id=user_id)
        customeraccount.usd = customeraccount.usd + companyaccounthistory.usd
        customeraccount.save()
        customerexpenseshistory = CustomerExpensesHistory.objects.get(uniq_id=uniq_id)
        customerexpenseshistory.delete()
        companyaccounthistory.delete()
    return redirect('companymoney')


def addcompanyownexpenses(request):
    if request.method == 'POST':
        form = CompanyOwnExpensesHistoryForm(request.POST)
        companyaccount = CompanyAccount.objects.get(pk=1)
        companyexpenses = CompanyExpenses.objects.get(pk=1)
        if form.is_valid():
            companyaccount.usd = companyaccount.usd - float(request.POST['usd'])
            companyexpenses.usd = companyexpenses.usd + float(request.POST['usd'])
            companyexpenses.save()
            companyaccount.save()
            obj = form.save(commit=False)
            obj.uniq_id = str(random.randint(1000, 9999))
            obj.user_id = request.POST['user_id']
            obj.staff_id = request.user.id
            obj.description = request.POST['description'] + " || " + str(
                request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
            obj.save()
            couriername = User.objects.get(pk=request.POST['user_id'])
            message = "--------Затрата-------\nКурер: {} {}" \
                      "\nВ Долларах: {}" \
                      "\nДата: {}".format(couriername.last_name,
                                          couriername.first_name,
                                          request.POST['usd'],
                                          datetime.today().strftime('%Y-%m-%d'))
            bot = telegram.Bot(token=settings.BOT_TOKEN_EXP)
            bot.sendMessage(chat_id=settings.BOT_CHAT_ID_EXP, text=message)
            return redirect('companyownexpenseshistorys')
    else:
        form = CompanyOwnExpensesHistoryForm()
        currency = CurrencyHistory.objects.all().last()
        objectlist = UserProfile.objects.exclude(role='клиент').select_related('user')
    return render(request, 'staff/addcompanyexpenses.html',
                  {"form": form, "currency": currency, "objectlist": objectlist})


def editcompanyownexpenses(request, id):
    if request.method == 'POST':
        pi = CompanyOwnExpensesHistory.objects.get(pk=id)
        print(pi.usd)
        money = CompanyOwnExpensesHistoryForm(request.POST, instance=pi)
        if money.is_valid():
            obj = money.save(commit=False)
            obj.staff_id = request.user.id
            obj.description = request.POST['description'] + " || " + str(request.POST['usd_rub'] + " || " + request.POST['usd_uzs'])
            companyaccount = CompanyAccount.objects.get(pk=1)
            companyaccount.usd = companyaccount.usd + pi.usd
            companyaccount.save()
            companyaccountnew = CompanyAccount.objects.get(pk=1)
            companyaccountnew.usd = companyaccountnew.usd - float(request.POST['usd'])
            companyaccountnew.save()
            money.save()
            return redirect('companyownexpenseshistorys')
    else:
        pi = CompanyOwnExpensesHistory.objects.get(id=id)
        money = CompanyOwnExpensesHistoryForm(instance=pi)
    currency = CurrencyHistory.objects.all().last()
    description = CompanyOwnExpensesHistory.objects.get(id=id)
    customerlist = UserProfile.objects.filter(role='курер').select_related('user')
    return render(request, 'staff/editcompanyownexpenses.html',
                  {"money": money,  "description":description, "customerlist":customerlist,"currency": currency})


def deletemoneyfromownexpenses(request, id):
    deletemoneyfromownexpenses = CompanyOwnExpensesHistory.objects.get(pk=id)
    companyexpenese = CompanyExpenses.objects.get(pk=1)
    companyexpenese.usd = companyexpenese.usd - deletemoneyfromownexpenses.usd
    companyexpenese.save()
    companyaccount = CompanyAccount.objects.get(pk=1)
    companyaccount.usd = companyaccount.usd + deletemoneyfromownexpenses.usd
    companyaccount.save()
    deletemoneyfromownexpenses.delete()
    return redirect('companyownexpenseshistorys')
