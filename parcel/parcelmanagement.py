from django.shortcuts import render, redirect
from currency.models import *
from userprofile.models import *
from django.http import JsonResponse
from parcel.forms import *
import json
from parcel.models import *
from customer.models import *
from company.models import *

def addparcel(request):
    form = ParcelItemsForm()
    parcelmainmodel = ParcelMain()
    currency = CurrencyHistory.objects.all().last()
    parcelplans = ParcelPlan.objects.all()
    customerlist = UserProfile.objects.filter(role='клиент').select_related('user')
    courierlists = UserProfile.objects.filter(role='курер').select_related('user')
    if request.method == 'POST' and request.is_ajax():
        print(request.POST.get('parcel_getmoney_foritem'))
        parcelmainmodel.uniq_id = str(random.randint(1000, 9999))
        parcelmainmodel.sender_id = request.POST.get('sender_id')
        parcelmainmodel.recipient_id = request.POST.get('recipient_id')
        parcelmainmodel.staff_sender_id = request.user.id
        parcelmainmodel.parcel_status_id = 9
        print(request.POST.get('parcel_getmoney_foritem'))
        if request.POST.get('parcel_getmoney_foritem') != 'on':
            parcelmainmodel.parcel_getmoney_foritem = request.POST.get('parcel_getmoney_foritem')
        else:
            parcelmainmodel.parcel_getmoney_foritem = 'off'
        parcelmainmodel.parcel_plan_id = request.POST.get('parcel_plan_id')
        print(request.POST.get('parcel_weight'))
        if request.POST.get('parcel_plan_id') == '1' or '3' or '5' or '7' or '8':
            parcelmainmodel.parcel_from = 'Москва -> Ташкент'
        elif request.POST.get('parcel_plan_id') == '2' or '4' or '6':
            parcelmainmodel.parcel_from = 'Ташкент -> Москва'
        if request.POST.get('parcel_plan_id') == '1' or '2' and request.POST.get('parcel_weight') == "":
            parcelmainmodel.parcel_weight = 2
        elif request.POST.get('parcel_plan_id') == '3' or '4' or '5' or '6' and request.POST.get('parcel_weight') == "":
            parcelmainmodel.parcel_weight = 1
        elif request.POST.get('parcel_plan_id') == '1' or '2' or '3' or '4' or '5' or '6' and request.POST.get('parcel_weight') != "":
            parcelmainmodel.parcel_weight = request.POST.get('parcel_weight')
        # if request.POST.get('parcel_dostavka_courier_id') != '':
        parcelmainmodel.courier_dostavka_id = request.POST.get('parcel_dostavka_courier_id')
        # if request.POST.get('parcel_zabor_courier_id') != '':
        parcelmainmodel.courier_zabor_id = request.POST.get('parcel_zabor_courier_id')
        parcelmainmodel.parcel_cost = request.POST.get('parcel_cost')
        parcelmainmodel.parcel_zabor_cost = request.POST.get('parcel_zabor_cost')
        parcelmainmodel.parcel_width = request.POST.get('parcel_width')
        parcelmainmodel.parcel_height = request.POST.get('parcel_height')
        parcelmainmodel.parcel_length = request.POST.get('parcel_length')
        parcelmainmodel.parcel_dimension = request.POST.get('parcel_dimension')
        parcelmainmodel.parcel_zabor = request.POST.get('parcel_zabor')
        parcelmainmodel.parcel_dostavka = request.POST.get('parcel_dostavka')
        parcelmainmodel.parcel_description = request.POST.get('parcel_description') + " || " + str(
            request.POST.get('usd_rub') + " || " + request.POST.get('usd_uzs'))
        if 'parcel_image' in request.FILES:
            file1 = request.FILES['parcel_image']
            parcelmainmodel.parcel_image = file1
        if 'parcel_report_image' in request.FILES:
            file2 = request.FILES['parcel_report_image']
            parcelmainmodel.parcel_report_image = file2

        parcelmainmodel.save()
        c = ParcelMain.objects.latest('id')

        parcelstatushistorymodel = ParcelStatusHistory()
        parcelstatushistorymodel.parcelmain_id = c.pk
        parcelstatushistorymodel.parcel_status_id = 9
        parcelstatushistorymodel.save()

        dict_list = json.loads(request.POST.get('html_data'))
        if (len(dict_list['myRows']) != 0):
            for x in dict_list['myRows']:
                parcelitemsmodel = ParcelItems()
                parcelitemsmodel.parcelmain_id = c.pk
                parcelitemsmodel.prod_name = x['Название']
                parcelitemsmodel.prod_url = x['Ссылка на товар']
                parcelitemsmodel.prod_cnt = x['Количество']
                parcelitemsmodel.prod_cost = x['Цена (за шт)']
                parcelitemsmodel.prod_tnved = x['ТНВЭД']
                parcelitemsmodel.prod_weight = x['Вес']
                parcelitemsmodel.save()
        return JsonResponse({'message': 'success'})
    else:
        form = ParcelItemsForm()
    return render(request, 'parcel/addparcel.html',
                  {'form': form, "customerlist": customerlist, "courierlists": courierlists, "currency": currency,
                   "parcelplans": parcelplans})


def listparcel(request):
    parcelmainmodels = ParcelMain.objects.all()
    return render(request, 'parcel/listparcel.html', {'parcelmainmodels': parcelmainmodels})


def parcelview(request, id):
    parcelmainmodel = ParcelMain.objects.get(pk=id)
    parcelitems = ParcelItems.objects.filter(parcelmain_id=id)
    parcelstatushistorys = ParcelStatusHistory.objects.filter(parcelmain_id=id)

    return render(request, 'parcel/parcelview.html', {'parcelmainmodel': parcelmainmodel, 'parcelitems': parcelitems,
                                                      'parcelstatushistorys': parcelstatushistorys})


def deleteparcel(request, id):
    ParcelStatusHistory.objects.filter(parcelmain_id=id).delete()
    ParcelItems.objects.filter(parcelmain_id=id).delete()
    ParcelMain.objects.get(pk=id).delete()
    return redirect('listparcel')


def editparcel(request, id):
    parcel_couriers = UserProfile.objects.filter(role='курер').select_related('user')
    parcelstatuses = ParcelStatusName.objects.all()
    parcelmainmodel = ParcelMain.objects.get(pk=id)
    currency = CurrencyHistory.objects.all().last()
    parcelplans = ParcelPlan.objects.all()
    customerlist = UserProfile.objects.filter(role='клиент').select_related('user')
    parcelitems = ParcelItems.objects.filter(parcelmain_id=id)
    if request.method == 'POST' and request.is_ajax():

        parcelmainmodel.parcel_cost = request.POST.get('parcel_cost')
        parcelmainmodel.parcel_weight = request.POST.get('parcel_weight')
        if request.POST.get('parcel_status') == '16':
            print(parcelmainmodel.parcel_getmoney_foritem)
            print(parcelmainmodel.recipient_id)
            customerexpenseshistory = CustomerExpensesHistory()
            customerexpenseshistory.uniq_id = str(random.randint(1000, 9999))
            customerexpenseshistory.user_id = parcelmainmodel.recipient_id
            customerexpenseshistory.service_type = 'За перевозку Москва-Ташкент'
            customerexpenseshistory.description = request.POST.get('parcel_description')
            customerexpenseshistory.usd = parcelmainmodel.parcel_cost
            customerexpenseshistory.staff_id = request.user.id
            customerexpenseshistory.save()

            customeraccount = CustomerAccount.objects.get(user_id=parcelmainmodel.recipient_id)
            customeraccount.usd = float(customeraccount.usd) - float(parcelmainmodel.parcel_cost)
            customeraccount.save()

            companyaccounthistory = CompanyAccountHistory()
            companyaccounthistory.uniq_id = str(random.randint(1000, 9999))
            companyaccounthistory.user_id = parcelmainmodel.recipient_id
            companyaccounthistory.usd = parcelmainmodel.parcel_cost
            companyaccounthistory.description = request.POST.get('parcel_description')
            companyaccounthistory.staff_id = request.user.id
            companyaccounthistory.service_type = 'За перевозку Москва-Ташкент'
            companyaccounthistory.plan_type = request.POST.get('parcel_plan_id')
            companyaccounthistory.save()

            companyaccount = CompanyAccount.objects.get(pk=1)
            companyaccount.usd = float(companyaccount.usd) + float(parcelmainmodel.parcel_cost)
            companyaccount.save()

            print(parcelmainmodel.parcel_cost)

        parcelmainmodel.parcel_status_id = request.POST.get('parcel_status')
        parcelmainmodel.courier_dostavka_id = request.POST.get('parcel_dostavka_courier_id')
        parcelmainmodel.courier_zabor_id = request.POST.get('parcel_zabor_courier_id')
        parcelmainmodel.parcel_description = request.POST.get('parcel_description') + " || <br>asd</br>" + str(
            request.POST.get('usd_rub') + " || " + request.POST.get('usd_uzs'))
        if 'parcel_image' in request.FILES:
            file1 = request.FILES['parcel_image']
            parcelmainmodel.parcel_image = file1
        if 'parcel_report_image' in request.FILES:
            file2 = request.FILES['parcel_report_image']
            parcelmainmodel.parcel_report_image = file2
        parcelmainmodel.save()
        ParcelItems.objects.filter(parcelmain_id=id).delete()
        dict_list = json.loads(request.POST.get('html_data'))
        if (len(dict_list['myRows']) != 0):
            for x in dict_list['myRows']:
                parcelitemsmodel = ParcelItems()
                parcelitemsmodel.parcelmain_id = id
                parcelitemsmodel.prod_name = x['Название']
                parcelitemsmodel.prod_url = x['Ссылка на товар']
                parcelitemsmodel.prod_cnt = x['Количество']
                parcelitemsmodel.prod_cost = x['Цена (за шт)']
                parcelitemsmodel.prod_tnved = x['ТНВЭД']
                parcelitemsmodel.prod_weight = x['Вес']
                parcelitemsmodel.save()

        laststatus_id = ParcelStatusHistory.objects.filter(parcelmain_id=id).last()
        # print(laststatus_id.parcel_status.id)
        # print(request.POST.get('parcel_status'))
        if laststatus_id.parcel_status.id != int(request.POST.get('parcel_status')):
            parcelstatushistorymodel = ParcelStatusHistory()
            parcelstatushistorymodel.parcelmain_id = id
            parcelstatushistorymodel.parcel_status_id = request.POST.get('parcel_status')
            parcelstatushistorymodel.save()

        # print(request.POST)
        return JsonResponse({'message': 'success'})
    else:
        form = ParcelItemsForm()
    return render(request, 'parcel/editparcel.html', {
        'parcelmainmodel': parcelmainmodel,
        'parcelstatuses': parcelstatuses,
        'parcel_couriers': parcel_couriers,
        'currency': currency,
        'parcelplans': parcelplans,
        'customerlist': customerlist,
        'parcelitems': parcelitems
    })
