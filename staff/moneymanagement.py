from django.http import JsonResponse
from django.shortcuts import render, redirect
from customer.models import *
from customer.forms import *
from django.db import connection
from main.models import *
from userprofile.models import *
from company.models import *
import telegram
from django.conf import settings
from datetime import datetime
from currency.models import *

def listmoney(request):
    listmoneys = CustomerAccountHistory.objects.all().select_related('user')
    loans = CustomerLoan.objects.get(user_id=request.user.id)
    randomm = str(random.randint(1000, 9999))
    return render(request, 'staff/listmoney.html', {"listmoneys": listmoneys, "loans": loans, "random": randomm})


def elistmoney(request, uniq_id, user_id):
    print(uniq_id)
    customeraccounthistory = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
    customeraccount = CustomerAccount.objects.get(user_id=user_id)
    if customeraccounthistory.general_status == 'В обработке':
        customeraccounthistory.general_status = 'Одобрено'
        customeraccount.usd = customeraccount.usd + customeraccounthistory.usd
        customeraccount.rub = customeraccount.rub + customeraccounthistory.rub
        customeraccount.uzs = customeraccount.uzs + customeraccounthistory.uzs
    elif customeraccounthistory.general_status == 'Одобрено':
        customeraccounthistory.general_status = 'В обработке'
        customeraccount.usd = customeraccount.usd - customeraccounthistory.usd
        customeraccount.rub = customeraccount.rub - customeraccounthistory.rub
        customeraccount.uzs = customeraccount.uzs - customeraccounthistory.uzs
    customeraccount.save()
    customeraccounthistory.save()
    return redirect('stafflistmoney')


def addmoney(request):
    if request.method == 'POST':
        print(request.POST['user_id'])
        form = CustomerAccountHistoryForm(request.POST)
        customeraccount = CustomerAccount.objects.get(user_id=request.POST['user_id'])
        if form.is_valid():
            customeraccount.usd = customeraccount.usd + float(request.POST['usd'])
            customeraccount.rub = customeraccount.rub + float(request.POST['rub'])
            customeraccount.uzs = customeraccount.uzs + float(request.POST['uzs'])
            customeraccount.save()
            obj = form.save(commit=False)
            obj.uniq_id = str(random.randint(1000, 9999))
            obj.general_status = 'Одобрено'
            obj.user_id = request.POST['user_id']
            obj.save()
            customername = User.objects.get(pk=request.POST['user_id'])
            message = "--------Пополнение баланса-------\nКлиент: {} {}" \
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
            return redirect('stafflistmoney')
    else:
        form = CustomerAccountHistoryForm()
        currency = CurrencyHistory.objects.all().last()
        objectlist = UserProfile.objects.filter(role='клиент').select_related('user')
    return render(request, 'staff/addmoney.html', {"form": form, "objectlist": objectlist, "currency":currency})


def editmoney(request, uniq_id):
    if request.method == 'POST':
        pi = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
        money = CustomerAccountHistoryForm(request.POST, instance=pi)
        if money.is_valid():
            money.save()
            return redirect('stafflistmoney')
    else:
        pi = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
        money = CustomerAccountHistoryForm(instance=pi)
    currency = CurrencyHistory.objects.all().last()
    return render(request, 'staff/editmoney.html', {"money": money, "currency":currency})


def deletemoney(request, uniq_id):
    customeraccounthistory = CustomerAccountHistory.objects.get(uniq_id=uniq_id)
    customeraccounthistory.delete()
    return redirect('stafflistmoney')
